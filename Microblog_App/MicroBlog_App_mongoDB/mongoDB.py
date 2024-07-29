from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "your_connection_string"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.microblog