import random
from database import get_connection
from datetime import datetime, timedelta

# constant values for payment methods and order statuses
PAYMENT_METHODS = ['Credit Card', 'Debit Card', 'UPI', 'Cash on Delivery', 'Net Banking', 'Wallet']
ORDER_STATUSES = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled', 'Returned']


#get data from the database
def get_customer_ids_from_database():
    connection = get_connection()
    if connection is None:
        return []

    cursor = connection.cursor()
    cursor.execute("SELECT CustomerID FROM Customers")
    customer_ids = [row[0] for row in cursor.fetchall()]
    connection.close()
    return customer_ids


# generate random customer ID from the list of customer IDs
def generate_random_customer_id(customer_ids):
    return random.choice(customer_ids)

# generate random order date within the last 3 years
def generate_random_order_date():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=1095)  # 3 years ago
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime('%Y-%m-%d %H:%M:%S')

# generate random payment method from the list of payment methods
def generate_random_payment_method():
    return random.choice(PAYMENT_METHODS)

# generate random order status from the list of order statuses
def generate_random_order_status():
    return random.choice(ORDER_STATUSES)

# generate random order data
def generate_random_order_data(customer_ids):
    order_data = {
        'CustomerID': generate_random_customer_id(customer_ids),
        'OrderDate': generate_random_order_date(),
        'PaymentMethod': generate_random_payment_method(),
        'OrderStatus': generate_random_order_status()
    }
    return order_data


# generate orders data
def generate_orders_data(num_orders):
    customer_ids = get_customer_ids_from_database()
    orders_data = []
    for _ in range(num_orders):
        order_data = generate_random_order_data(customer_ids)
        orders_data.append(order_data)
    return orders_data


#Testing the function
"""if __name__ == "__main__":
    num_orders = 10  # specify the number of orders to generate
    print(generate_orders_data(num_orders))

    for order in generate_orders_data(num_orders):
        print(order)"""