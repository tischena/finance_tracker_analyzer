"""
Creates and returns a SQLAlchemy engine for connecting to the PostgreSQL database.

The function reads database connection parameters from the configuration file
and builds a PostgreSQL connection URL using psycopg2.

Returns:
    sqlalchemy.engine.Engine: A SQLAlchemy engine instance used for running
    database queries and transactions.
"""

from sqlalchemy import create_engine
from config import config

def get_engine():
    params = config()
    engine_url = f"postgresql+psycopg2://{params['user']}:{params['password']}@{params['host']}/{params['database']}"
    return create_engine(engine_url)












