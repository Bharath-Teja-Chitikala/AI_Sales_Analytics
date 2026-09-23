import pandas as pd
from database import get_connection

# This script retrieves sales transaction data from the database and displays a summary of the retrieved data. It uses the `get_connection` function from the `database` module to establish a connection to the database, executes a SQL query to fetch all records from the `vw_SalesTransactions` view, and handles any exceptions that may occur during the process. Finally, it prints out the first few records, total number of records retrieved, and the column names in the dataset.
def get_sales_by_transactions():
    connection = get_connection()
    if connection is None:
        print("Failed to establish a database connection.")
        return None
    query = "SELECT * FROM vw_SalesTransactions"
    try:
        sales_data = pd.read_sql(query, connection)
        print("Data retrieved successfully.")
        return sales_data
    except Exception as e:
        print(f"Error occurred while retrieving data: {e}")
        return None
    finally:
        connection.close()

# This function retrieves sales KPI data from the database and returns it as a pandas DataFrame. It establishes a connection to the database using the `get_connection` function, executes a SQL query to fetch all records from the `vw_SalesKPIs` view, and handles any exceptions that may occur during the process. Finally, it closes the database connection and returns the retrieved data.
def get_sales_by_kpi():
    connection = get_connection()
    if connection is None:
        print("Failed to establish a database connection.")
        return None
    query = "SELECT * FROM vw_SalesKPIs"
    try:
        sales_kpi = pd.read_sql(query, connection)
        print("Sales KPI data retrieved successfully.")
        return sales_kpi
    except Exception as e:
        print(f"Error occurred while retrieving Sales KPI data: {e}")
        return None
    finally:
        connection.close()

# This function retrieves sales data by products from the database and returns it as a pandas DataFrame. It establishes a connection to the database using the `get_connection` function, executes a SQL query to fetch all records from the `vw_SalesByProduct` view, and handles any exceptions that may occur during the process. Finally, it closes the database connection and returns the retrieved data.
def get_sales_by_products():
    connection = get_connection()
    if connection is None:
        print("Failed to establish a database connection.")
        return None
    query = "SELECT * FROM vw_SalesByProduct"
    try:
        sales_by_products = pd.read_sql(query, connection)
        print("Sales by Products data retrieved successfully.")
        return sales_by_products
    except Exception as e:
        print(f"Error occurred while retrieving Sales by Products data: {e}")
        return None
    finally:
        connection.close()

# This function retrieves sales data by category from the database and returns it as a pandas DataFrame. It establishes a connection to the database using the `get_connection` function, executes a SQL query to fetch all records from the `vw_SalesByCategory` view, and handles any exceptions that may occur during the process. Finally, it closes the database connection and returns the retrieved data.
def get_sales_by_category():
    connection = get_connection()
    if connection is None:
        print("Failed to establish a database connection.")
        return None
    query = "SELECT * FROM vw_SalesByCategory"
    try:
        sales_by_category = pd.read_sql(query, connection)
        print("Sales by Category data retrieved successfully.")
        return sales_by_category
    except Exception as e:
        print(f"Error occurred while retrieving Sales by Category data: {e}")
        return None
    finally:
        connection.close()

# This function retrieves sales data by customer from the database and returns it as a pandas DataFrame. It establishes a connection to the database using the `get_connection` function, executes a SQL query to fetch all records from the `vw_SalesByCustomer` view, and handles any exceptions that may occur during the process. Finally, it closes the database connection and returns the retrieved data.
def get_sales_by_customer():
    connection = get_connection()
    if connection is None:
        print("Failed to establish a database connection.")
        return None
    query = "SELECT * FROM vw_SalesByCustomer"
    try:
        sales_by_customer = pd.read_sql(query, connection)
        print("Sales by Customer data retrieved successfully.")
        return sales_by_customer
    except Exception as e:
        print(f"Error occurred while retrieving Sales by Customer data: {e}")
        return None
    finally:
        connection.close()

# This function retrieves sales data by date from the database and returns it as a pandas DataFrame. It establishes a connection to the database using the `get_connection` function, executes a SQL query to fetch all records from the `vw_SalesByDate` view, and handles any exceptions that may occur during the process. Finally, it closes the database connection and returns the retrieved data.
def get_sales_by_date():
    connection = get_connection()
    if connection is None:
        print("Failed to establish a database connection.")
        return None
    query = "SELECT * FROM vw_SalesByDate"
    try:
        sales_by_date = pd.read_sql(query, connection)
        print("Sales by Date data retrieved successfully.")
        return sales_by_date
    except Exception as e:
        print(f"Error occurred while retrieving Sales by Date data: {e}")
        return None
    finally:
        connection.close()

# This function retrieves sales data by order status from the database and returns it as a pandas DataFrame. It establishes a connection to the database using the `get_connection` function, executes a SQL query to fetch all records from the `vw_SalesByOrderStatus` view, and handles any exceptions that may occur during the process. Finally, it closes the database connection and returns the retrieved data.
def get_sales_by_order_status():
    connection = get_connection()
    if connection is None:
        print("Failed to establish a database connection.")
        return None
    query = "SELECT * FROM vw_SalesByOrderStatus"
    try:
        sales_by_order_status = pd.read_sql(query, connection)
        print("Sales by Order Status data retrieved successfully.")
        return sales_by_order_status
    except Exception as e:
        print(f"Error occurred while retrieving Sales by Order Status data: {e}")
        return None
    finally:
        connection.close()

# This function retrieves sales data by payment method from the database and returns it as a pandas DataFrame. It establishes a connection to the database using the `get_connection` function, executes a SQL query to fetch all records from the `vw_SalesByPaymentMethod` view, and handles any exceptions that may occur during the process. Finally, it closes the database connection and returns the retrieved data.
def get_sales_by_payment_method():
    connection = get_connection()
    if connection is None:
        print("Failed to establish a database connection.")
        return None
    query = "SELECT * FROM vw_SalesByPaymentMethod"
    try:
        sales_by_payment_method = pd.read_sql(query, connection)
        print("Sales by Payment Method data retrieved successfully.")
        return sales_by_payment_method
    except Exception as e:
        print(f"Error occurred while retrieving Sales by Payment Method data: {e}")
        return None
    finally:
        connection.close()

# This function retrieves sales data by brand from the database and returns it as a pandas DataFrame. It establishes a connection to the database using the `get_connection` function, executes a SQL query to fetch all records from the `vw_SalesByBrand` view, and handles any exceptions that may occur during the process. Finally, it closes the database connection and returns the retrieved data.
def get_sales_by_brand():
    connection = get_connection()
    if connection is None:
        print("Failed to establish a database connection.")
        return None
    query = "SELECT * FROM vw_SalesByBrand"
    try:
        sales_by_brand = pd.read_sql(query, connection)
        print("Sales by Brand data retrieved successfully.")
        return sales_by_brand
    except Exception as e:
        print(f"Error occurred while retrieving Sales by Brand data: {e}")
        return None
    finally:
        connection.close()

# This function retrieves sales profitability data from the database and returns it as a pandas DataFrame. It establishes a connection to the database using the `get_connection` function, executes a SQL query to fetch all records from the `vw_SalesProfitability` view, and handles any exceptions that may occur during the process. Finally, it closes the database connection and returns the retrieved data.
def get_sales_profitability():
    connection = get_connection()
    if connection is None:
        print("Failed to establish a database connection.")
        return None
    query = "SELECT * FROM vw_SalesProfitability"
    try:
        sales_profitability = pd.read_sql(query, connection)
        print("Sales Profitability data retrieved successfully.")
        return sales_profitability
    except Exception as e:
        print(f"Error occurred while retrieving Sales Profitability data: {e}")
        return None
    finally:
        connection.close()


#vw_SalesByBrand vw_SalesByCategory vw_SalesByCustomer vw_SalesByDate vw_SalesByOrderStatus vw_SalesByPaymentMethod vw_SalesByProduct vw_SalesKPIs vw_SalesProfitability vw_SalesTransactions

if __name__ == "__main__":
   # sales_data = get_sales_data()
    #if sales_data is not None:
     # print("\nSales Transaction:")
     # print(sales_data.head())
     # print(f"Total records retrieved: {len(sales_data)}")
     # print(f"Columns in the dataset: {sales_data.columns.tolist()}") 

# for saleskpi function
   # sales_kpi = get_sales_kpi()
   # if sales_kpi is not None:
   #     print("\nSales KPI Data:")
   #     print(sales_kpi.head())
   #     print(f"Total records retrieved: {len(sales_kpi)}")
   #     print(f"Columns in the dataset: {sales_kpi.columns.tolist()}")

   if __name__ == "__main__":

    analytics_functions = {
        "Sales By Product": get_sales_by_products,
        "Sales By Category": get_sales_by_category,
        "Sales By Brand": get_sales_by_brand,
        "Sales By Customer": get_sales_by_customer,
        "Sales By Date": get_sales_by_date,
        "Sales By Order Status": get_sales_by_order_status,
        "Sales By Payment Method": get_sales_by_payment_method,
        "Sales Profitability": get_sales_profitability
    }

    for name, function in analytics_functions.items():

        print(f"\n{'=' * 60}")
        print(f"{name}")
        print(f"{'=' * 60}")

        data = function()

        if data is not None:
            print(data.head())
            print(f"Total records retrieved: {len(data)}")
            print(f"Columns in the dataset: {data.columns.tolist()}")
        else:
            print(f"Failed to retrieve {name} data.")