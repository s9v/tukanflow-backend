from pymongo import MongoClient

# Database config
MONGO_IP = 'localhost'
MONGO_PORT = '27017'
DB_NAME = 'tukanflow'
# ===

client = MongoClient(f'mongodb://{MONGO_IP}:{MONGO_PORT}/')
# client = MongoClient('mongodb+srv://admin:junction2021@cluster0.tybky.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client[DB_NAME]

# Collections
documents_coll = db['documents']
users_coll = db['users']
meetings_coll = db['meetings']

def get_database():
    return db
