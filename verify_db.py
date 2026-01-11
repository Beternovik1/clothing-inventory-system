import mysql.connector
from db_config import get_db_config

def verify_table_structure(table_name):
    config = get_db_config()
    connection = None
    cursor = None
    
    try:
        # 1. Connect
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        
        # 2. Inspect
        print(f"\n--- INSPECTING: {table_name} ---")
        cursor.execute(f"DESCRIBE {table_name}")
        
        # 3. Print Header
        print(f"{'Field':<15} {'Type':<15} {'Null':<5} {'Key':<5}")
        print("-" * 45)

        # 4. Print Rows
        for row in cursor:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<5} {row[3]:<5}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        # 5. The Safety Net
        # We check if 'cursor' and 'connection' exist before closing
        # to avoid errors if the connection failed at the very start.
        if cursor:
            cursor.close()
            print("\nCursor closed.")
        if connection:
            connection.close()
            print("Connection closed.")

# Main execution
if __name__ == "__main__":
    verify_table_structure('products')