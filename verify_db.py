import mysql.connector
from db_config import get_db_config

config = get_db_config()
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

print("Tables in database")
cursor.execute("Show tables")
for table in cursor:
    print(table[0])

table_name = 'products'
try:
    cursor.execute(f'Describe {table_name}')
    print(f'{'Field':<15} {'Type':<15} {'Null':<5} {'Key':<5}')
    print("-" * 45)

    for row in cursor:
        # row format: (Field, Type, Null, Key, Default, Extra)
        print(f"{row[0]:<15} {row[1]:<15} {row[2]:<5} {row[3]:<5}")
except mysql.connector.Error as err:
    print(f'Error: {err}')

cursor.close()
connection.close()