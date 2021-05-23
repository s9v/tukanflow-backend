from pymongo import MongoClient

# Database config
MONGO_IP = 'localhost'
MONGO_PORT = '27017'
DB_NAME = 'myFirstDatabase'
# ===

client = MongoClient(f'mongodb://{MONGO_IP}:{MONGO_PORT}/')
# client = MongoClient('mongodb+srv://admin:junction2021@cluster0.tybky.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client[DB_NAME]

# Collections
stages = db['stages']

try:
    resume_token = None
    pipeline = [{'$match': {'operationType': 'insert'}}]
    with stages.collection.watch(pipeline) as stream:
        for insert_change in stream:
            print(insert_change)
            resume_token = stream.resume_token
            # TODO
except pymongo.errors.PyMongoError:
    
