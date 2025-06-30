import psycopg2
from config import host, user, password, db_name

table_name = ''

def create_table(name):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        
        connection.autocommit = True
        
        with connection.cursor() as cursor:
            cursor.execute(
                f"""CREATE TABLE {name}(
                    id serial PRIMARY KEY,
                    product VARCHAR(50) NOT NULL,
                    price DECIMAL(10,2),
                    sale_date DATE
                    )"""
            )
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()