# Transaction Categorization and Database Pipeline

## Table of Contents

* [About](#about)
* [Features](#features)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Database](#database)
* [Visualization](#visualization)

## About

This Data Engineering project demonstrates a complete ETL pipeline for personal transaction data. The pipeline extracts data from Excel files, categorizes transactions using a rule-based approach, loads them into a PostgreSQL database, and visualizes insights in Power BI.

## Features

* Automates extraction of transaction data from Excel files.
* Applies rule-based transaction categorization.
* Loads categorized data into PostgreSQL with a structured schema.
* Supports analytics and visualization in Power BI.
* Ensures data integrity and traceability in the database.

## Getting Started

### Prerequisites

* Python 3.9 or later
* PostgreSQL installed and running
* SQLAlchemy and psycopg2 for database connections
* Pandas library for data processing
* Access to Excel files containing transaction data
* Power BI for visualization (optional, for dashboards)

### Installation

1.Clone the repository:

```bash
git clone <repo-url>
cd <repo-folder>
```

2.Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3.Install dependencies:

```bash
pip install -r requirements.txt
```

4.Configure your PostgreSQL database credentials in `config.py` or the `.ini` file.

5.Initialize the database schema:

```bash
psql -f schema.sql -U <username> -d <database_name>
```

## Usage

The pipeline consists of three main stages:

1.**Extract** – Load raw transaction data from an Excel file:

```bash
python extract_from_excel.py
```

2.**Transform** – Clean and categorize the transactions:

```bash
python categorize_transactions.py
```

3.**Load** – Insert the categorized data into PostgreSQL:

```bash
python load_to_database.py
```

Once data is loaded, use Power BI to connect to the database and visualize spending patterns.

## Database

* **Configuration:** `config.py` reads database credentials from `.ini` files.
* **Engine:** `connection.py` uses SQLAlchemy to connect to PostgreSQL.
* **Schema:** `schema.sql` creates two tables:
  * `categories` – Stores unique category names.
  * `transactions` – Stores individual transactions with category references.

## Visualization

* Power BI dashboards visualize:

  * Spending breakdown by category
  * Trends over time
  * Comparison of different spending areas
* The dashboards use the PostgreSQL tables as their data source.
