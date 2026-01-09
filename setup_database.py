# mysql.connector knows hot to take a python command
# and convert it into a specific bunary message that
# MySQL server understands
import mysql.connector
# get_db_config pull the passwrods of the db form the .env file
from db_config import get_db_config

def create_tables():
    config = get_db_config()
    
    with open('pants_db.sql', 'r') as file:
        sql_script = file.read()

    connection = None
    try:
        # With **config we convert the dictionary with the data from db_config
        # and we pass it as a tuple with separate arguments to connect to 
        # the db
        connection = mysql.connector.connect(**config)

        # with cursor we point to each command to execute
        with connection.cursor() as cursor:
            # using split(';') to split the text at every ';' and create a 
            # list of individual sql commands since execute() function
            # can just run just one SQL command at a time
            commands = sql_script.split(';')
            for command in commands:
                # removing all invisible whitespace with strip()
                if command.strip():
                    # executing each sql command
                    cursor.execute(command)
            # saving changes
            connection.commit()
            print("Database created !")
    except mysql.connector.Error as err:
        print(f'Error:{err}')
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed")
        
if __name__ == "__main__":
    create_tables()
        
