from psycopg2 import connect, extras

from config import Config

host = Config.host
port = Config.port
dbname = Config.dbname
user = Config.user
password = Config.password

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn
    