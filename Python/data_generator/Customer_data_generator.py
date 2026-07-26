#from multiprocessing.dummy import connection

from faker import Faker
import random
from datetime import datetime, timedelta  

from database import get_connection
# Initialize Faker and other variables
fake = Faker("en_US")

# Constant values for generating random data
Gender = ["Male", "Female"]

Customer_Segments = ["Regular","Silver","Gold","Platinum"]

Email_Providers = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
  
Locations = [("Hyderabad", "Telangana"), ("Bangalore", "Karnataka"), ("Chennai", "Tamil Nadu"), ("Mumbai", "Maharashtra"), ("Delhi", "Delhi"), ("Kolkata", "West Bengal"), ("Pune", "Maharashtra"), ("Ahmedabad", "Gujarat"), ("Jaipur", "Rajasthan"), ("Lucknow", "Uttar Pradesh"), ("Chandigarh", "Chandigarh"), ("Indore", "Madhya Pradesh"), ("Nagpur", "Maharashtra"), ("Bhubaneswar", "Odisha"), ("Coimbatore", "Tamil Nadu"), ("Visakhapatnam", "Andhra Pradesh"), ("Patna", "Bihar"), ("Surat", "Gujarat"), ("Vadodara", "Gujarat"), ("Mysore", "Karnataka"), ("Vijayawada", "Andhra Pradesh"), ("Rajkot", "Gujarat"), ("Varanasi", "Uttar Pradesh"), ("Nashik", "Maharashtra"), ("Thiruvananthapuram", "Kerala"),  ("Jabalpur", "Madhya Pradesh"), ("Guwahati", "Assam"), ("Dehradun", "Uttarakhand"),  ("Amritsar", "Punjab"),  ("Jodhpur", "Rajasthan"),  ("Ranchi", "Jharkhand"),  ("Agra", "Uttar Pradesh"),  ("Durgapur", "West Bengal"),  ("Kolhapur", "Maharashtra"),  ("Mangalore", "Karnataka") ,  ("Udaipur","Rajasthan") ,  ("Tiruchirappalli","Tamil Nadu"), ("Gwalior","Madhya Pradesh"), ("Jammu","Jammu and Kashmir"), ("Srinagar","Jammu and Kashmir"), ("Shimla","Himachal Pradesh"), ("Gangtok","Sikkim"), ("Aizawl","Mizoram"), ("Kohima","Nagaland"), ("Itanagar","Arunachal Pradesh"), ("Agartala","Tripura"), ("Panaji","Goa")]

Countries = ["India"]


# Helper functions to generate random data
def get_gender():
    return random.choice(Gender)

def get_customer_segment():
    return random.choices(Customer_Segments, weights = [60,20,15,5])[0]

def get_email_provider(first_name, last_name):
    domain = random.choice(Email_Providers)
    return (
        f"{first_name.lower()}."
        f"{last_name.lower()}"
        f"{random.randint(1, 999)}"
        f"@{domain}"
    )

def get_Customer_Join_Date():
    return fake.date_between(start_date="-5y", end_date="today")

# Function to generate random customer data

def generate_customer_data(num_customers):
    connection = get_connection()
    if connection is None:
        print("Failed to connect to the database. Exiting.")
        return

    cursor = connection.cursor()

    for _ in range(num_customers):
        
        #generate_customer_data(1000)
        first_name = fake.first_name()
        last_name = fake.last_name()
        CustomerEmail = get_email_provider(first_name, last_name)
        CustomerPhone = fake.numerify("9#########")
        CustomerGender = get_gender()
        DateOfBirth = fake.date_of_birth(minimum_age=18, maximum_age=70)
        CustomerCity, CustomerState = random.choice(Locations)
        CustomerCountry = random.choice(Countries)
        CustomerSegment = get_customer_segment()
        CustomerJoinDate = get_Customer_Join_Date()

        # Insert the generated data into the database
        insert_query = """
            INSERT INTO Customers (FirstName,
            LastName,  
           Gender,
           DateOfBirth,
           CustomerEmail, CustomerPhone, CustomerCity, CustomerState, CustomerCountry, CustomerSegment, CustomerJoinDate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        # Execute the insert query with the generated data
        cursor.execute(insert_query, (
            first_name,
            last_name,
            CustomerGender,
            DateOfBirth,
            CustomerEmail,
            CustomerPhone,
            CustomerCity,
            CustomerState,
            CustomerCountry,
            CustomerSegment,
            CustomerJoinDate
        ))
    # Commit the transaction and close the connection
    connection.commit()
    cursor.close()
    connection.close()
    print(f"{num_customers} customer records generated and inserted into the database successfully") 


    


