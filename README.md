# AI Sales Analytics

AI Sales Analytics is a Python and SQL Server based sales analytics project designed to generate, store, validate, and analyze realistic sales data.

The project is being developed in multiple phases, starting with database design and automated sales data generation, followed by data validation, sales analytics, and future AI-powered sales analysis.

## Project Objectives

The main objectives of this project are:

- Design a structured relational sales database.
- Generate realistic customer, product, order, and order-detail data using Python.
- Insert generated data into SQL Server.
- Validate database records and relationships.
- Calculate and analyze sales and revenue information.
- Build an AI-powered sales analysis layer.
- Provide useful business insights from sales data.

## Technology Stack

- **Python**
- **SQL Server**
- **pyodbc**
- **Git**
- **GitHub**
- **Visual Studio Code**

## Project Structure

````text
AI_SALES_ASSISTANT/
│
├── Database/
│
├── Python/
│   ├── data_generator/
│   │   ├── __init__.py
│   │   ├── Customer_data_generator.py
│   │   ├── Helper_Functions.py
│   │   ├── OrderDetails_data_generator.py
│   │   ├── Orders_data_generator.py
│   │   └── Product_data_generator.py
│   │
│   ├── ai_engine.py
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   └── insert_data.py
│
├── .gitignore
├── README.md
└── requirements.txt

## Database

The project uses SQL Server as the relational database.

The current sales database includes the following main entities:

Customers
Products
Orders
OrderDetails

The database uses primary keys, foreign keys, identity columns, and CHECK constraints to maintain data integrity.

## Data Generation

Python is used to generate realistic sample sales data.

The data generation modules include:

Customer_data_generator.py — generates customer information.
Product_data_generator.py — generates product information.
Orders_data_generator.py — generates order information.
OrderDetails_data_generator.py — generates order-detail records.
Helper_Functions.py — contains reusable helper functions.

The generated data is designed to follow the constraints and relationships defined in the SQL Server database.

## Data Insertion

The generated Python data is inserted into SQL Server using pyodbc.

The project includes:

database.py — database connection functionality.
insert_data.py — data insertion functionality.

## Data Validation

Database validation is an important stage of the project.

The validation process includes:

Record count validation.
Primary key validation.
Foreign key integrity validation.
Order and OrderDetails relationship validation.
Sales and revenue validation.

This ensures that the generated data is correctly stored and maintains the expected database relationships.

## AI Sales Analysis

The project also includes an AI-oriented analysis layer.

The ai_engine.py module is intended to provide the foundation for AI-powered sales analysis and business insights.

## Future analysis capabilities may include:

Sales performance analysis.
Revenue analysis.
Product performance analysis.
Customer analysis.
Sales trends.
Business recommendations.
Natural-language interaction with sales data.

## Application

The main application entry point is:

Python/app.py

The application will eventually connect the database, sales analytics functionality, and AI analysis components into a single workflow.

## Current Project Status

The project is currently under active development.

### Completed

- SQL Server database design.
- Customer data generator.
- Product data generator.
- Order data generator.
- OrderDetails data generator.
- Python-to-SQL Server database connection.
- Generated data insertion into SQL Server.
- Initial database validation phase.
- Git repository setup.
- GitHub repository setup.

### In Progress

- Complete database validation.
- Revenue validation.
- Sales analytics development.
- AI sales analysis functionality.

### Planned

- Advanced sales analytics.
- AI-powered business insights.
- Natural-language sales queries.
- Additional validation and testing.
- Improved application interface.
- Project documentation and deployment preparation.

## How to Run

### 1. Clone the repository
```bash
git clone <repository-url>
````

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

## Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Update the database configuration in:

```text
Python/config.py
```

## Make sure the SQL Server database is available and the required tables have been created.

### 5. Run the application

```bash
python Python/app.py
```

## Project Development

This project is being developed incrementally, with each phase focusing on a specific part of the overall AI Sales Analytics system.

The development process includes:

Database design
Data generation
Data insertion
Database validation
Sales analytics
AI-powered analysis
Application integration
Testing and documentation

## License

This project is currently being developed as a personal portfolio and learning project.
