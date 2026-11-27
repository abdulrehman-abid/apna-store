import mysql
import imports

def add_product(code, name, price, stock):
    connection = imports.connect_to_database()
    cursor = connection.cursor()
    try:
        insert_query = """
        INSERT INTO products (code, name, price, stock)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (code, name, price, stock))
        connection.commit()
        print("Product added successfully!")
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    
def show_products():
    connection = imports.connect_to_database()
    cursor = connection.cursor()
    try:
        select_query = "SELECT * FROM products"
        cursor.execute(select_query)
        products = cursor.fetchall()
        return products
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

if __name__ == "__main__":
    # Example usage
    add_product("P001", "Product 1", 10.99, 100)
    products = show_products()
    for product in products:
        print(product)