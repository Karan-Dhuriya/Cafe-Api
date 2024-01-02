from flask import Flask
from resources.item import blp as ItemBluePrint  # that '/item' link 
from resources.user import blp as UserBluePrint  # that '/user' link 
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from blocklist import BLOCK_LIST

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTION"] = True
app.config["API_TITLE"] = "Cafe Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config["JWT_SECRET_KEY"] = "75145022625505402875533839797188341356259104707964631188915326094540404746916"


api = Api(app)
jwt = JWTManager(app)


""" check token is alredy bloked if true then revoked_token_loader will be run """
@jwt.token_in_blocklist_loader
def check_if_token_in_block_list(jwt_header,jwt_payload):    # Refer link : jwt decode
    return jwt_payload['jti'] in BLOCK_LIST

@jwt.revoked_token_loader
def revoke_token_callback(jwt_header,jwt_payload):
    return {
        "description" : " User has been logged out. ",
        "error" : "token revoked"
    }

api.register_blueprint(ItemBluePrint)
api.register_blueprint(UserBluePrint)










































# # args == parameter they have passed and instead of get there is one more option which is getlist if you don't know which parameter/argumnets they are passing  
# @app.get('/items') #http://127.0.0.1:5000/get-items

# @app.get('/item')
# def get_item():
#     id = request.args.get('id')  
    
#     if id is None:
#         return {"items" : fruits_items}
    
#     try:
#         return fruits_items[id]
#     except:
#         return {"message" : "record doesn't exist"}
    
#     # and we can write like this too above lines
#     # try:
#     #     return fruits_items[request.args.get('id')]
#     # except:
#     #     return {"message" : "record doesn't exist"}


# @app.post('/item')
# def add_items():
#     requested_data = request.get_json()
#     if 'name' not in requested_data or 'price' not in requested_data:
#         return {"message" : "'name' and 'price' must be included"}
#     fruits_items[uuid.uuid4().hex] = requested_data
#     return {"message" : "Item added succesfully"}, 201

# # http://127.0.0.1:5000



# @app.put('/item')
# def update_items():
#     id = request.args.get('id')
#     if id == None:
#         return {"message" : "please enter valid ID"}
    
#     requested_data = request.get_json()
#     if 'name' not in requested_data or 'price' not in requested_data:
#         return {"message" : "'name' and 'price' must be included"}
    
#     if id in fruits_items.keys():
#         fruits_items[id] = requested_data
#         return {"message" : "item update suceessfully"}
#     return {"message" : "itme doesn't exist in record"}
        
    
    
# @app.delete('/item')
# def delete_item():
#     id = request.args.get('id') 
    
#     if id == None:
#         return {"message" : "please enter valid ID"}
     
#     if id in fruits_items.keys():
#         del fruits_items[id]
#         return {"mesage" : "item deleted successfully"}
#     return {"message" : "record doesn't exist"}





# @app.get('/get-items') #http://127.0.0.1:5000/get-items
# def get_items():
#     return {"items" : fruits_items}


# # @app.get('/get-item/<string:name>')
# # def get_item(name):
# #     for item in fruits_items:
# #         if name == item['name']:
# #             return item
# #     return {"message" : "record doesn't exist"}

# # Another way to access the single data if the have passed parameters  

# @app.get('/get-item')
# def get_item():
#     name = request.args.get('name')  # args == parameter they have passed and instead of get there is one more option which is getlist if you don't know which parameter/argumnets they are passing  
#     for item in fruits_items:
#         if name == item['name']:
#             return item
#     return {"message" : "record doesn't exist"}
    
    


# @app.post('/add-items')
# def add_items():
#     request_add = request.get_json()
#     fruits_items.append(request_add)
#     return {"message" : "Item added succesfully"}, 201

# # http://127.0.0.1:5000



# @app.put('/update-item')
# def update_items():
#     request_add = request.get_json()
#     for item in fruits_items:
#         if item['name']== request_add['name'] :
#             item['price'] = request_add['price']
#             return {"message" : "item update suceessfully"}
#     return {"message" : "itme doesn't exist in record"}
        
    
    
# @app.delete('/delete-item')
# def delete_item():
#     name = request.args.get('name')  
#     for item in fruits_items:
#         if name == item['name']:
#             fruits_items.remove(item)
#             return {"mesage" : "item deleted successfully"}
#     return {"message" : "record doesn't exist"}


