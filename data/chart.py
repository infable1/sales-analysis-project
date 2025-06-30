import psycopg2
from config import host, user, password, db_name
import pandas as pd
import matplotlib.pyplot as plt

def Paint(table_name='sales'):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
            
        connection.autocommit = True
        
        query = f"SELECT sale_date, SUM(price) AS daily_sales FROM {table_name} GROUP BY sale_date;"
        df = pd.read_sql(query, connection)

        plt.bar(df['sale_date'], df['daily_sales'])
        plt.xlabel('Date')
        plt.ylabel('Sales ($)')
        plt.title('Daily Sales')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'sales-analysis-project/data/{table_name}_plot.png')
        plt.show()
        

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
