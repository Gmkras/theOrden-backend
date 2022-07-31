import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVER_NAME= "localhost:7001"
    DEBUG = True
    
    host = os.environ.get('host')
    port = os.environ.get('port')
    dbname = os.environ.get('dbname')
    user = os.environ.get('user')
    password = os.environ.get('password')
    
    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"