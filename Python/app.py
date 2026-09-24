"""from database import get_connection 

def main():
    connection = get_connection()
    if connection:
        # Perform database operations here
        print("database is ready...")
        connection.close()
        print("database connection closed...")

if __name__ == "__main__":
    main()"""

# For generating customer data and inserting it into the database
"""from data_generator.Customer_data_generator import generate_customer_data

def main():
    num_customers = 1000  # Specify the number of customer records to generate
    generate_customer_data(num_customers)

if __name__ == "__main__":
    main()"""

# For generating order data and inserting it into the database
"""from data_generator.Orders_data_generator import generate_orders_data
from insert_data import insert_order_data

def main():
    num_orders = 100  # Specify the number of order records to generate
    orders_data = generate_orders_data(num_orders)
    insert_order_data(orders_data)  # Insert the generated order data into the database
    # insert_order_data(orders_data)

if __name__ == "__main__":
    main()"""

#For inserting order details data into database
#from data_generator.OrderDetails_data_generator import generate_order_details
#from insert_data import insert_order_details

#def main():
  #order_details_data=generate_order_details()
  #insert_order_details(order_details_data)

#if __name__=="__main__":
  #main()
  
## for app.py 

# ---------------------------------------------------------
# AI SALES ANALYTICS APPLICATION
# ---------------------------------------------------------

from analytics.sales_analytics import (
    get_sales_by_kpi,
    get_sales_by_products,
    get_sales_by_category,
    get_sales_by_brand,
    get_sales_by_customer,
    get_sales_by_date,
    get_sales_by_order_status,
    get_sales_by_payment_method,
    get_sales_profitability,
    get_sales_by_transactions
)


def display_result(title, analytics_function):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    data = analytics_function()

    if data is not None:
        print(data.to_string(index=False))
        print(f"\nTotal records retrieved: {len(data)}")
    else:
        print(f"Failed to retrieve {title} data.")


def main():

    analytics_options = {
        "1": ("Sales KPIs", get_sales_by_kpi),
        "2": ("Sales by Product", get_sales_by_products),
        "3": ("Sales by Category", get_sales_by_category),
        "4": ("Sales by Brand", get_sales_by_brand),
        "5": ("Sales by Customer", get_sales_by_customer),
        "6": ("Sales by Date", get_sales_by_date),
        "7": ("Sales by Order Status", get_sales_by_order_status),
        "8": ("Sales by Payment Method", get_sales_by_payment_method),
        "9": ("Sales Profitability", get_sales_profitability),
        "10": ("Sales Transactions", get_sales_by_transactions)
    }

    while True:

        print("\n" + "=" * 60)
        print("             SALES ANALYTICS PLATFORM")
        print("=" * 60)

        for option, (title, _) in analytics_options.items():
            print(f"{option}. {title}")

        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("\nExiting Sales Analytics Platform...")
            break

        if choice in analytics_options:

            title, analytics_function = analytics_options[choice]

            display_result(title, analytics_function)

        else:
            print("\nInvalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()