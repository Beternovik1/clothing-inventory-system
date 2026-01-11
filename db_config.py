import os
from dotenv import load_dotenv

# Loading variables from .env file
load_dotenv()

def get_db_config():
    return {
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('MYSQL_USER_PASS'),
        'database': os.getenv('DB_DATABASE')
    }

def get_sqlalchemy_url():
    user = os.getenv('DB_USER')
    password = os.getenv('MYSQL_USER_PASS')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db = os.getenv('DB_DATABASE')

    return f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}'

