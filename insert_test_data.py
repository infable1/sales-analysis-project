import random
from datetime import datetime, timedelta
import psycopg2
from config import host, user, password, db_name

def insert_test_data(table_name='sales', num_rows = 100):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        
        connection.autocommit = True
        
        with connection.cursor() as cursor:
            products = ["Laptop", "Phone", "Tablet", "Headphones", "Mouse", "Keyboard", "Monitor", "Charger"]

            price_range = (50.00, 1500.00)

            start_date = datetime(2025, 6, 1)
            end_date = datetime(2025, 6, 30)
            
            for _ in range(num_rows):
                product = random.choice(products)
                price = round(random.uniform(price_range[0], price_range[1]), 2)
                sale_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
                
                sql = f"INSERT INTO {table_name} (product, price, sale_date) VALUES (%s, %s, %s);"
                values = (product, price, sale_date)
                
                cursor.execute(sql, values)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()