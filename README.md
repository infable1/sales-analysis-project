# Sales Analysis Project

This project implements a comprehensive sales data analysis system using PostgreSQL and Python. It creates a sales database, inserts 500 test records, performs analytical queries, generates an Excel report, and visualizes daily sales trends. The code is structured for modularity and reusability.

## Features
- Creates a PostgreSQL table (`sales_j`) with columns for product, price, and sale date.
- Inserts 500 random test records for June 2025.
- Calculates total sales, average price per product, and daily sales amounts.
- Generates an Excel report (`data.xlsx`) with formatted data.
- Creates a bar chart of daily sales (`sales_j_plot.png`) using Matplotlib.
- Organizes output in a `sales-analysis-project/data` directory.

## Skills Demonstrated
- Python
- PostgreSQL (database management and SQL queries)
- Pandas (data handling)
- Matplotlib (data visualization)
- OpenPyXl (Excel report generation)
- File and folder management

## Project Structure
- `main.py`: Main script to orchestrate the project (table creation, data insertion, analysis, and plotting).
- `config.py`: Configuration file for database credentials (host, user, password, db_name).
- `create_table.py`: Script to create the sales table.
- `insert_test_data.py`: Script to insert test records.
- `analysis.py`: Script to perform SQL queries and generate an Excel report.
- `data/chart.py`: Script to generate a bar chart of daily sales.
- `sales-analysis-project/data/`: Directory for output files (Excel and plots).

## How to Run
1. Install required libraries: `pip install psycopg2-binary pandas matplotlib openpyxl`.
2. Configure `config.py` with your PostgreSQL credentials (host, user, password, db_name).
3. Ensure PostgreSQL is running and the database exists.
4. Run the main script: `python main.py`.
5. Check the `sales-analysis-project/data` folder for the Excel report and plot.

## Notes
- The project uses a test dataset for June 2025 with 500 entries.
- Database errors are handled with try-except blocks.
- The bar chart displays total daily sales; adjust `chart.py` for other visualizations if needed.
- Ensure proper permissions for file creation and database access.