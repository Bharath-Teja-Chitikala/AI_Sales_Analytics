from database import get_connection 

# Function to insert product data into the database
def insert_product_data(product_data):
    connection = get_connection()
    if connection is None:
        print("Failed to connect to the database. Data insertion aborted.")
        return

    cursor = connection.cursor()

    try:
        for product in product_data:
            cursor.execute("""
                INSERT INTO Product (Category,ProductType,Brand,ProductName,CostPrice,UnitPrice,Stock)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (product['Category'], product['ProductType'], product['Brand'], product['ProductName'], product['CostPrice'], product['UnitPrice'], product['Stock']))
        
        connection.commit()
        print("Product data inserted successfully.")

    except Exception as error:
        print("Error while inserting data into the database:", error)
        connection.rollback()

    finally:
        cursor.close()
        connection.close()



# Function to insert order data into the database
def insert_order_data(orders):
    connection = get_connection()
    if connection is None:
        print("Failed to connect to the database. Data insertion aborted.")
        return

    cursor = connection.cursor()

    try:
        for order in orders:
            cursor.execute("""
                INSERT INTO Orders (CustomerID,OrderDate,OrderStatus,PaymentMethod)
                VALUES (?, ?, ?, ?)
            """, (order['CustomerID'], order['OrderDate'], order['OrderStatus'], order['PaymentMethod']))

        connection.commit()
        print("Order data inserted successfully.")

    except Exception as error:
        print("Error while inserting data into the database:", error)
        connection.rollback()

    finally:
        cursor.close()
        connection.close()


#Function to insert order details data into database
def insert_order_details(order_details):
  connection = get_connection()
  if connection is None:
    return None

  cursor = connection.cursor()
  try:
    cursor.executemany("""INSERT INTO OrderDetails(OrderID,ProductID,Quantity,SellingPrice,Discount)
          VALUES(?,?,?,?,?)""",order_details)
    connection.commit()
    print("Insert is succesfull")
  except Exception as error:
        print("Error as ",error)
        connection.rollback()
  finally:
        cursor.close()
        connection.close()