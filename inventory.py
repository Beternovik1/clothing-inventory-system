import mysql.connector
from db_config import get_connection

#   CREATE
def add_product(category, color, size, cost_price, sell_price, currently_stock):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        # SQL query inserting data
        # %s is a place holder that convert the value into the value we inserted it
        sql = """
            INSERT INTO products (category, color, size, cost_price, sell_price, currently_stock)
                VALUES (%s, %s, %s, %s, %s, %s)
        """

        # data tuple
        values = (category, color, size, cost_price, sell_price, currently_stock)
        cursor.execute(sql, values)
        connection.commit()

        # cursor.lastrowid is an id number the db assign to the item i created from the 
        # cursor's memory
        print(f'Success !, Product added with ID: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if cursor:
            cursor.close()
            print('Cursor closed')
        if connection and connection.is_connected():
            connection.close()
            print('Connection closed')

# READ
def get_products():
    connection = None
    cursor = None
    results = []
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            SELECT * 
                FROM products
                WHERE is_active = 1
        """

        cursor.execute(sql)
        # Getting all the results with fetchall converting them as a list
        results = cursor.fetchall()

        # print('------ CURRENT STOCK -------')
        # for product in results:
        #     print(product)
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
    return results

# UPDATE 
def update_stock(product_id, new_stock):   
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            UPDATE products 
                SET currently_stock = %s 
                WHERE product_id = "%s"
        """
        values = (new_stock, product_id)
        cursor.execute(sql, values)
        connection.commit()

        # Checking if the row was actually updated
        if cursor.rowcount == 0:
            print(f'Error: Product ID {product_id} not found.')
        else:
            print(f'Success !, Product with id : {product_id} stock updated to {new_stock}')
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
    
# DELETE
def delete_stock(product_id):
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            UPDATE products
                SET is_active = 0
                WHERE product_id = %s
        """
        values = (product_id, )
        cursor.execute(sql, values)
        connection.commit()

        # Checking if we actually deleted something
        if cursor.rowcount == 0:
            print(f'Error: Product ID {product_id} not found')
        else:
            print(f'Success!, product ID {product_id} deleted')
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    print(get_products())