from flask import Flask, request
from flask_restful import Api, abort
import uuid
from database.user import UserDatabase
from flask_smorest import Blueprint
from flask.views import MethodView
from schemas import SuccessMessage, UserSchema,UserQuerySchema
import hashlib
from flask_jwt_extended import create_access_token,get_jwt, jwt_required
from blocklist import BLOCK_LIST

blp = Blueprint("user", __name__, description ="Operation on users")


@blp.route('/login')
class UserLogin(MethodView):
    def __init__(self):
        self.db = UserDatabase()
        
    @blp.arguments(UserSchema)
    def post(self, request_data):
        username = request_data["username"]
        password = hashlib.sha256(request_data["password"].encode('utf-8')).hexdigest()
        user_id = self.db.Verify_user(username,password)
        if user_id:
            return {"access token" : create_access_token(identity = user_id) }
        abort(404, message ="username or password is incorrect")

@blp.route('/logout')
class UserLogout(MethodView):
    
    @jwt_required() 
    def post(self):
        BLOCK_LIST.add(get_jwt()["jti"] )
        return {"message" : "successfully logged out."}


@blp.route('/user')
class User(MethodView):
    
    """ here we are going to call our data base one time"""
    def __init__(self):
        self.db = UserDatabase()  #we will use this object for all the methods in class
    
    """ To fetch the data from data base"""
    @blp.response(200, UserSchema)
    @blp.arguments(UserQuerySchema, location="query")
    def get(self, args):
        person_id = args.get('person_id')
        result = self.db.get_user(person_id)
        if result is None:
            abort(404, message ="user does not exist")
        return result

    """ For adding data """
    @blp.arguments(UserSchema)
    @blp.response(200, SuccessMessage)
    def post(self, request_data):
        username = request_data["username"]
        password = hashlib.sha256(request_data["password"].encode('utf-8')).hexdigest()
        """
        encode() which is used to convert a string to bytes, meaning that the string can be passed
        into the sha256 function
        hexdigest() which is used to convert our data into hexadecimal format
        """
        if self.db.add_user(username, password):
            return {"message" : "user added succesfully"}, 201
        abort(404, message ="user already exist") 
    
    """ To deleting the data """
    @blp.response(200, SuccessMessage)
    @blp.arguments(UserQuerySchema, location= "query")
    def delete(self,args):
        person_id = args.get('person_id') 
        if self.db.delete_user(person_id):
            return {"message" : "user deleted"}
        abort(404, message ="user doesn't exist")  