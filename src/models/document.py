from db import documents_coll
from pymongo import InsertOne, DeleteOne, ReplaceOne

def get_document(id):
    return documents_coll.find_one({"id": id})

def set_document(id, document):
    documents_coll.replace_one({"id": id}, document, True)
