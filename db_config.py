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
