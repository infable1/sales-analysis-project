import psycopg2
from config import host, user, password, db_name

from create_table import create_table
from insert_test_data import insert_test_data
from analysis import analysis
from data.chart import Paint

create_table('sales_j')
insert_test_data('sales_j', 500)
analysis('sales_j')
Paint('sales_j')