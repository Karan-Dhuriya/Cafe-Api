import pyodbc

class UserDatabase:
    def __init__(self):      #constructor because we don't to run the server again and again
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=KARAN_DHURIYA;DATABASE=cafe;')
        self.cursor = self.conn.cursor()


    def get_user(self, person_id):
        query = f"SELECT * FROM users where person_id = {person_id}"
        self.cursor.execute(query)    
        user_dict ={}           
        result = self.cursor.fetchone()
        if result is not None:
            user_dict['person_id'], user_dict['username'], user_dict['password']  = result
            return user_dict
            
        
    def add_user(self, username, password):    
        query = f"INSERT INTO users (username,password) VALUES ('{username}','{password}')"
        try:
            self.cursor.execute(query)
            self.conn.commit()  # make sure to commit the query otherwise it won't gonna show in database
            return True
        except pyodbc.IntegrityError:
            return False
        
    
    def delete_user(self, person_id):
        query = f"DELETE FROM users WHERE person_id = {person_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True
        
    
    def Verify_user(self,username,password):
        query = f"SELECT * FROM users WHERE username = '{username}' and  password = '{password}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result is not None:
            return result[0]
        
        
