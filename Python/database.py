import pyodbc
from config import CONNECTION_STRING

def get_connection():
   try:
    Connection = pyodbc.connect(CONNECTION_STRING)
    print("Connection to the database was successful.")
    return Connection

   except Exception as error:
    print("Error while connecting to the database:", error)
    return None
