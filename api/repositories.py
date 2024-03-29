from django.conf import settings
import pymongo
import uuid

class ClassRepository:
    
    collection = ''
    
    def __init__(self, collection_name) -> None:
        self.collection = collection_name
        
    def get_connection(self):
        client = pymongo.MongoClient(
            getattr(settings, "MONGO_CONNECTION_STRING"))
        connection = client[
            getattr(settings, "MONGO_DATABASE_NAME")]
        return connection
        
        
    def get_collection(self):
        conn = self.get_connection()
        collection = conn[self.collection]
        return collection
    
    def get_all(self):
        document = self.get_collection().find({})
        return document
    
    def get_by_id(self, id):
        document = self.get_collection().find_one({"id": id})
        return document
    
    def insert(self, document):
        data = {
            "id": str(uuid.uuid4()),
            "nome":document["nome"], 
            "responsavel": document["responsavel"]
        }
        self.get_collection().insert_one(data)
        
    def drop_all(self):
        self.get_collection().drop()
        
    def update(self, query, data):
        self.get_collection().update_one(query, {"$set": data})

    def delete(self, query):
        self.get_collection().delete_one(query)