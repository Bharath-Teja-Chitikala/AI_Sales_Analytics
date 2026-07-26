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
from data_generator.OrderDetails_data_generator import generate_order_details
from insert_data import insert_order_details

def main():
  order_details_data=generate_order_details()
  insert_order_details(order_details_data)

if __name__=="__main__":
  main()
  

