import psycopg2
from config import config

def connect():
    connection = None
    """Create a database connection using the configuration file."""
    
    # Create a connection to the PostgreSQL database
    try:
        params = config()
        connection = psycopg2.connect(**params)
        print("Connection to the database established successfully.")
        #return connection
        crsr = connection.cursor()
        #print('PostgreSQL database version:')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        #print(db_version)
        crsr.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print("Database connection closed.")
            
if __name__ == "__main__":
    connect()

# connection = psecopg2.connect(host = "localhost",
#                               port = "5432",
#                               database = "anas_transactions_proj",
#                               user = "postgres",
#                               password = "1234567890")