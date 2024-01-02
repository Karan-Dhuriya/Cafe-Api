from flask import Flask, request
from flask_restful import Api, abort
import uuid
from database.item import ItmeDatabse
from flask_smorest import Blueprint
from flask.views import MethodView
from schemas import ItemGetSchema, ItmesSchema, SuccessMessage ,ItemQuerySchema , ItemOptinalQuerySchema
from flask_jwt_extended import jwt_required

blp = Blueprint("items", __name__, description ="Operation on items")


@blp.route('/item')
class Item(MethodView):
    
    """ here we are going to call our data base one time"""
    def __init__(self):
        self.db = ItmeDatabse()  #we will use this object for all the methods in class
    
    """ To fetch the data from data base"""
    """@jwt_required() just for verify the access token"""
    @jwt_required()                                
    @blp.response(200, ItemGetSchema(many=True))
    @blp.arguments(ItemOptinalQuerySchema, location= "query")
    def get(self, args):
        id = args.get('id')  
        
        if id is None:
            return self.db.get_items()
        else:
            result = self.db.get_item(id)
            if result is None:
                abort(404, message ="Record does not exist")
            return result
    
    """ To Update the data  """    
    @jwt_required()
    @blp.arguments(ItmesSchema)
    @blp.response(200, SuccessMessage)
    @blp.arguments(ItemQuerySchema, location= "query")
    def put(self, request_data, args):
        id = args.get('id')
        if self.db.update_items(id,request_data):
            return {"message" : "item update suceessfully"}
        abort(404, message ="item doesn't exist in record")

    """ For adding data """
    @jwt_required()
    @blp.arguments(ItmesSchema)
    @blp.response(200, SuccessMessage)
    def post(self, request_data):
        id  = uuid.uuid4().hex
        self.db.add_items(id,request_data)
        return {"message" : "Item added succesfully"}, 201
    
    
    """ To deleting the data """
    @jwt_required()
    @blp.response(200, SuccessMessage)
    @blp.arguments(ItemQuerySchema, location= "query")
    def delete(self,args):
        id = args.get('id') 
        if self.db.delete_items(id):
            return {"message" : "item deleted"}
        abort(404, message ="record doesn't exist")  