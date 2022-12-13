import pymongo
import os
from dotenv import load_dotenv

def mongo_conn():
    try:
        conn = pymongo.MongoClient(os.getenv('ID_MONGODB')) # default config mongodb localhost
        print("Mongo connected\n")
        return conn.grid_file
    except Exception as e:
        print("Erro in mongo connection:", e)