import mysql.connector
from db_config import get_db_config

def test_connection():
    config = get_db_config()
    print(f'Connecting with {config['database']}...')

    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Python is connected to the Docker Database !!")
            connection.close()
    except mysql.connector.Error as err:
        print(f'Error: {err}')

if __name__ == "__main__":
    test_connection()