# Sales Analytics Platform

Sales Analytics Platform is an end-to-end sales data analytics project built using Python and SQL Server, with Power BI planned as the visualization layer.

The project focuses on generating realistic sales data with Python, storing it in a structured SQL Server database, validating data integrity, creating reusable SQL analytics views, and performing sales analysis through Python.

The project was initially planned to include an AI-powered sales analysis component. However, the current implementation focuses on building a reliable data and analytics foundation. AI/LLM integration is planned as a future enhancement.

## Project Objectives

The main objectives of this project are:

- Design a structured relational sales database.
- Generate realistic customer, product, order, and order-detail data using Python.
- Insert the generated data into SQL Server.
- Maintain data integrity using primary keys, foreign keys, identity columns, and CHECK constraints.
- Validate generated sales data and database relationships.
- Build a reusable SQL analytics layer using database views.
- Develop reusable Python analytics functions.
- Prepare the data for business intelligence and visualization using Power BI.
- Establish a foundation for future AI/LLM-powered sales analysis.

## Technology Stack

- Python
- SQL Server
- Pandas
- pyodbc
- Faker
- NumPy
- Git
- GitHub
- Visual Studio Code
- Power BI — upcoming dashboard phase

## Project Architecture

The current project follows this workflow:

```text
Python Data Generation
        │
        ▼
    SQL Server
        │
        ├── Data Validation
        │
        ├── Revenue Validation
        │
        └── Reusable SQL Analytics Views
                    │
                    ▼
             Python Analytics
                    │
                    ▼
          Power BI Dashboard
              (Upcoming)
```

### Future Enhancement

```text
Sales Analytics Foundation
            │
            ▼
       AI / LLM Layer
            │
            ├── Natural-language sales queries
            ├── Automated business insights
            └── AI-assisted sales analysis
```

## Database

The project uses SQL Server as the relational database.

The sales database contains the following main entities:

- Customers
- Products
- Orders
- OrderDetails

The database uses:

- Primary keys
- Foreign keys
- Identity columns
- CHECK constraints
- Relational integrity rules

These database constraints help maintain consistent and valid sales data.

## Python Data Generation

Python is used to generate realistic sample sales data.

The data-generation modules include:

### Customer Data

`Customer_data_generator.py`

Generates customer information for insertion into SQL Server.

### Product Data

`Product_data_generator.py`

Generates product information including:

- Category
- Product type
- Brand
- Product name
- Cost price
- Unit price
- Stock

### Order Data

`Orders_data_generator.py`

Generates order information including:

- Order date
- Order status
- Payment method
- Customer relationship

### Order Details

`OrderDetails_data_generator.py`

Generates order-level product details including:

- Order
- Product
- Quantity
- Selling price
- Discount

### Helper Functions

`Helper_Functions.py`

Contains reusable functions used by the data-generation modules.

## Data Insertion

Generated Python data is inserted into SQL Server using `pyodbc`.

The main components include:

### `database.py`

Provides the database connection functionality.

### `insert_data.py`

Handles the insertion of generated data into SQL Server.

The Python-to-SQL Server connection and data insertion workflow have been completed and validated.

## Data Validation

Data validation was performed to ensure that the generated data was correctly stored and maintained the required relationships.

The validation process includes:

- Record count validation
- Primary key validation
- Foreign key integrity validation
- Order and OrderDetails relationship validation
- Sales and revenue validation

### Validated Data

| Table        | Records |
| ------------ | ------: |
| Customers    |   1,000 |
| Products     |     500 |
| Orders       |     100 |
| OrderDetails |     299 |

Primary key validation confirmed that the expected IDs are unique.

Foreign key validation confirmed valid relationships between:

- Orders → Customers
- OrderDetails → Orders
- OrderDetails → Products

Order-level validation also confirmed that each order has at least one corresponding OrderDetails record.

## SQL Analytics Layer

A reusable SQL analytics layer was developed to avoid repeatedly writing standalone analytical queries.

The project uses SQL Server views to provide reusable analytical datasets for downstream analysis.

The analytics layer includes views covering areas such as:

- Sales transactions
- Revenue analysis
- Order analysis
- Customer analysis
- Product performance
- Category performance
- Payment method analysis
- Order status analysis
- Monthly sales analysis
- Customer-level sales analysis

These views provide a consistent analytical foundation for the Python analytics layer and the planned Power BI dashboard.

## Python Analytics Layer

The project includes a reusable Python analytics module:

`Python/analytics/sales_analytics.py`

The module connects to SQL Server and consumes the reusable SQL analytics views to perform sales analysis using pandas.

The analytics functionality covers:

- Overall sales KPIs
- Revenue analysis
- Order analysis
- Customer analysis
- Product performance
- Category performance
- Payment method analysis
- Order status analysis
- Monthly sales analysis
- Customer-level sales analysis

The Python analytics layer is designed to consume the reusable SQL analytics layer rather than repeatedly rebuilding the underlying SQL logic.

## Power BI Dashboard

Power BI is the next major phase of the project.

The planned dashboard will use the prepared SQL analytics foundation to present sales information through interactive business intelligence visuals.

Planned areas include:

- Revenue KPIs
- Sales performance
- Order analysis
- Product performance
- Category performance
- Customer analysis
- Monthly sales trends
- Payment and order-status analysis

This section of the README will be updated with the actual dashboard, visuals, KPIs, and business insights after the Power BI phase is completed.

## AI / LLM Integration

AI/LLM integration is not currently implemented in the project.

The original project concept included an AI-powered sales analysis component. The current development has instead focused on building the underlying data and analytics foundation required for such a system.

Future AI/LLM capabilities may include:

- Natural-language questions about sales data
- Automated sales insights
- Revenue and performance explanations
- Product and customer analysis
- Sales trend interpretation
- AI-generated business insights
- Natural-language interaction with the analytics database

This component will be considered a future enhancement after the core analytics and Power BI implementation are completed.

## Project Structure

```text
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
│   ├── analytics/
│   │   ├── __init__.py
│   │   └── sales_analytics.py
│   │
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   └── insert_data.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment on Windows

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the database

Update the database configuration in:

```text
Python/config.py
```

Make sure SQL Server is available and the required database and tables have been created.

### 6. Run the analytics application

```bash
python Python/app.py
```

The application provides a command-line menu for accessing the available sales analytics functions, including KPIs, product analysis, category analysis, customer analysis, profitability, and sales transactions.

## Current Project Status

### Completed

- SQL Server database design
- Customer data generation
- Product data generation
- Order data generation
- OrderDetails data generation
- Python-to-SQL Server connection
- Generated data insertion
- Database validation
- Revenue validation
- Reusable SQL analytics views
- Python analytics layer
- Python analytics testing and code cleanup
- Git repository setup
- GitHub repository setup

### Current Phase

**AI-SALES-21 — Documentation + GitHub Portfolio Polish**

### Next Phase

**AI-SALES-22 — Power BI Dashboard**

### Future Enhancement

- AI/LLM-powered sales analysis
- Natural-language sales queries
- Automated business insights
- AI-assisted sales analytics

## Development Approach

The project was developed incrementally, with each phase building on the previous layer:

```text
1. Database Design
       ↓
2. Python Data Generation
       ↓
3. Data Insertion
       ↓
4. Database Validation
       ↓
5. Revenue Validation
       ↓
6. Reusable SQL Analytics Layer
       ↓
7. Python Analytics Layer
       ↓
8. Power BI Dashboard (Upcoming)
       ↓
9. Future AI / LLM Integration
```

This layered approach separates data generation, storage, validation, analytics, visualization, and future AI capabilities, making the project easier to maintain and extend.

## License

This project is developed as a personal portfolio and learning project.
