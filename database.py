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
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL
            )
        """)
        connection.commit()
        print("Tables created successfully!")
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