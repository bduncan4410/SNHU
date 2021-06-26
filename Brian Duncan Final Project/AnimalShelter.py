from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import ast

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        try:
            
            self.client = MongoClient('mongodb://AACAdmin:admin@127.0.0.1:50220/AAC')
            self.database = self.client['AAC']
            print("Database Connected")
        except:
            print("ERROR: Database Not Connected")
            
            
    # Read method that take a query and passes it to the db
    def createOne(self, data):
        if data is not None:    # If the data is not empty
            return self.database.AAC.insert_one(data)  # data should be dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method that takes data and inserts in into the collection
    def createMany(self, data):
        if data is not None:    # If the data is not empty
            return self.database.AAC.insert_many(data)  # data should be dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method that take a query and passes it to the db
    def read(self, query):
        if query is not None:
            return self.database.AAC.find_one(query)  # passes the query to the database
        else:
            return self.database.AAC.find()
            

    #Update method that takes a query formatted as such:
    # { "name": "Brian" }
    # and  new values formatted like above and updates the value in the db
    def update(self, query, newValues):
        try:
            return self.database.AAC.update_one(query, newValues);
        except:
            print("Document Not Found");
            return;
      
        
        
    # Delete method that takes a query formatted as such:
    # { "name": "Brian" }
    # and  new values formatted like above and updates the value in the db
    def delete(self, query):
        try:
           return self.database.AAC.delete_one(query)
        except:
            print("Document Not Found");
            return;

    # Method that formats the query string in the appropriate manner.
    #Accepts an id and the value and creates a string to pass into the CRUD methods.
    def formatQuery(self, id, value):
        query = { id:  value}
        return query
                 
 


