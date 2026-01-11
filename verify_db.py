import mysql.connector
# We import the get_db_function object itself but we don't 
# add () at the end because we're NOT running it yet
from db_config import get_db_config

def verify_db(table_name):
    connection = None
    cursor = None

    try:
        config = get_db_config()
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        print("Tables in database")
        cursor.execute("Show tables")


        for table in cursor:
            print(table[0])

        # Describe is an sql command that shows the structure of the table (only the column names,
        # data types, and if a column can be empty/null)
        cursor.execute(f'Describe {table_name}')
        print(f'{'Field':<15} {'Type':<15} {'Null':<15} {'Key':<15}')
        print("-" * 45)

        for row in cursor:
            # row format: (Field, Type, Null, Key, Default, Extra)
            print(f'{row[0]:<15} {row[1]:<15} {row[2]:<15} {row[3]:<15}')
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if cursor:
            cursor.close()
            print("Cursor closed")
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed")

if __name__ == "__main__":
    verify_db('products')
    # verify_db('inventory_movements')

    



