# Create your create_conn function to return a database connection object    #
from pg8000.native import Connection
import os
import dotenv

dotenv.load_dotenv()

user = os.environ['USER']
password = os.environ['PASSWORD']
db = os.environ['DATABASE']

def create_conn():
    conn = Connection(user, database = db, password = password)
    return conn

conn = create_conn()    

# Create a close_db function that closes a passed database connection object #

def close_db(conn):
    conn.close()

close_db(conn)