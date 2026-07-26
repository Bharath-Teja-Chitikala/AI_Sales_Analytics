import random
from database import get_connection

#Constants
DISCOUNT = [0, 5, 10, 15, 20]

#Function to generate order_ID
def get_order_id():
  connection = get_connection()
  if connection is None:
    return None

  cursor = connection.cursor()
  cursor.execute("""SELECT OrderID from Orders""")
  OrderIds = [row[0] for row in cursor.fetchall()]
  cursor.close()
  connection.close()  
  return OrderIds


def get_product_details():
  connection = get_connection()
  if connection is None:
    return None

  cursor = connection.cursor()
  cursor.execute("""SELECT ProductID, CostPrice, UnitPrice from Product""")
  product_details = [(row[0], row[1], row[2]) for row in cursor.fetchall()]
  cursor.close()
  connection.close()  
  return product_details

#Function to generate Quantity
def generate_quantity():
  return random.randint(1, 5)

#Function to generate Discount
def generate_discount():
  return random.choice(DISCOUNT)

#Function to generate selling price
def generate_selling_price(unit_price, discount):
  return round(float(unit_price) * (1 - discount / 100), 2)

#Function to generate order details
def generate_order_details():
  orderIds = get_order_id()
  product_details= get_product_details()
  if orderIds is None or product_details is None:
    return None
  order_details = []

  for orderId in orderIds:
    number_of_products = random.randint(1, 5)
    selected_products = random.sample(product_details, number_of_products)
    for product in selected_products:
      product_id, cost_price, unit_price = product
      quantity = generate_quantity()
      discount = generate_discount()
      selling_price = generate_selling_price(unit_price, discount)
      order_details.append((orderId, product_id, quantity, selling_price,discount ))
  return order_details

  
    


