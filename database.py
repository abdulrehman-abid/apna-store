import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port = 3306,
            user='root',
            password= os.getenv('MYSQL_ROOT_PASSWORD'),
            database='apna_store'
            
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def create_tables(connection):
    try:
        cursor = connection.cursor()

        tables = [
            """
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                role VARCHAR(50) NOT NULL,
                salary DECIMAL(10,2) NOT NULL,
                phone VARCHAR(20)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS products (
                product_id INT AUTO_INCREMENT PRIMARY KEY,
                code VARCHAR(20) UNIQUE NOT NULL,
                name VARCHAR(100) NOT NULL,
                price DECIMAL(10,2) NOT NULL CHECK (price > 0),
                stock INT NOT NULL CHECK (stock >= 0)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_name VARCHAR(100) NOT NULL,
                total_amount DECIMAL(10,2) NOT NULL,
                sale_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                employee_id INT,
                FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS sale_items (
                item_id INT AUTO_INCREMENT PRIMARY KEY,
                sale_id INT NOT NULL,
                product_code VARCHAR(20) NOT NULL,
                quantity INT NOT NULL CHECK (quantity > 0),
                price_at_sale DECIMAL(10,2) NOT NULL,
                FOREIGN KEY (sale_id) REFERENCES sales(sale_id)
            )
            """
        ]

        for table_sql in tables:
            cursor.execute(table_sql)

        connection.commit()
        print("Tables created successfully!")
        cursor.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
if __name__ == "__main__":
    db_connection = connect_to_database()
    if db_connection:
        print("Connected to the database successfully!")
        create_tables(db_connection)
        db_connection.close()
    else:
        print("Failed to connect to the database.")