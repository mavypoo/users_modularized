from flask_app.config.mysqlconnection import connectToMySQL # Allow us to connect to MySQL




class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full(self):
        return f"{self.first_name} {self.last_name}"
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        results = connectToMySQL('users_schema').query_db( query, data )
        return results
            # users_schema is the database name

    @classmethod
    def get_one(cls, data): # Data needed - we need the ID of the specific user
        query = "SELECT * FROM users WHERE id= %(id)s;"
        results = connectToMySQL('users_schema').query_db( query, data)
        return cls(results[0]) # We need a zero here [0] because its the first dictionary


    @classmethod 
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, created_at=NOW(), updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id= %(id)s;"
        return connectToMySQL('users_schema').query_db( query, data )

