from marshmallow import Schema, fields

class ItmesSchema(Schema):
    name = fields.Str(required=True)  #this thing here taking input and validating there type 
    price =  fields.Int(required=True)
    
    #we have to change this in items.py there is no required to take inputs and provide message
    
class ItemGetSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)  
    price =  fields.Int(dump_only=True)
    
"""For the success message"""
class SuccessMessage(Schema):
    message = fields.Str(dump_only=True)
    
"""for the perticular Api which is required ID like PUT and DELETE"""    
class ItemQuerySchema(Schema):
    id = fields.Str(required=True)
    
"""for the perticular Api which is not required ID like get and post"""    
class ItemOptinalQuerySchema(Schema):
    id = fields.Str(required=False)

class UserSchema(Schema):
    person_id = fields.Int(dump_only=True)
    username = fields.Str(required=True)  
    password =  fields.Str(required=True, load_only=True)
    
    
"""this is for that perticular API where id is required """
class UserQuerySchema(Schema):
    person_id = fields.Int(required=True)