from flask import Flask
from dotenv import load_dotenv
import os
from .routes import init_routes

load_dotenv()
db_password = os.getenv('DB_PASSWORD')

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://root:{db_password}@cluster0.j7kdz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("ping")
except Exception as e:
    print(e)

def create_app():
    app = Flask('website')

    #config 
    #security key, test mode, debugging window 

    # Register the routes by calling init_routes
    init_routes(app)

    return app