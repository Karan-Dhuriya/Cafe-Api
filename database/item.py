import pyodbc

class ItmeDatabse:
    def __init__(self):      #constructor because we don't to run the server again and again
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=KARAN_DHURIYA;DATABASE=cafe;')
        self.cursor = self.conn.cursor()


    def get_items(self):
        result = []     # we need to return list 
        query = "SELECT * FROM items"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}                # this is because we are getting data in tuple 
            item_dict['id'], item_dict['name'], item_dict['price']  = row
            result.append(item_dict)
        return result
            
            
    def get_item(self, item_id):
        query = f"SELECT * FROM items WHERE id = '{item_id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}                
            item_dict['id'], item_dict['name'], item_dict['price']  = row
        return [item_dict]
        
    
    def add_items(self,id, body):               # Add Items
        query = f"INSERT INTO items (id, name, price) VALUES ('{id}', '{body['name']}', {body['price']})"
        self.cursor.execute(query)
        self.conn.commit()  # make sure to commit the query otherwise it won't gonna show in database
        print("item added successfully")
    
    def update_items(self,id, body):                # Update Items
        query = f"UPDATE items SET name = '{body['name']}', price = {body['price']} WHERE id = '{id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True
    
    def delete_items(self, item_id):
        query = f"DELETE FROM items WHERE id = '{item_id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True
        
       

# db = ItmeDatabse()
# db.get_item('b79bc0a5eb874de7b75d51f1990df188')
# db = ItmeDatabse()
# db.post_items(id = 'b79bc0a5eb874de7b75d51f1990df189',body= {'name' : 'tea', 'price' : 69} )
# db = ItmeDatabse()
# db.update_items(id = '0329530d1ec74a25becf8b9e7003ac4awer', body= {'name' : 'Flat White', 'price' : 199} )





# fruits_items = [
#     {
#         "id" : "baebab1b79d849fcbafe5346573ec142",
#             "item" :
#                     {"name": "mango", "price": 100},
#     },
#     {
#         "id" : "8be15025afb24d92aefe221fc91fe2b5",
#             "item" :
#                     {"name": "banana", "price": 200},
#     },
#     {
#         "id" : "98ecdd6e7b9d43d29c9a607af08141d7",
#             "item" :
#                     {"name": "strawberry", "price": 400},
#     },
#     {
#         "id" : "1752e19dd2e645af8b04d7e30971e81c",
#              "item" :
#                      {"name": "black current", "price": 500}
#     }
    
# ]

