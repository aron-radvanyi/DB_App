# Database Converter Application 

## Overview

This Python application connects to a MySQL database, displays its tables in a graphical interface, and allows exporting selected tables to CSV files.

## Prerequisites

- Python 3.9 or later
- MySQL database
- [Virtualenv](https://virtualenv.pypa.io/) (optional but recommended)

## Installation

1. Clone the repository:

   cli:
   git clone 

2. Navigate to the project directory:
    cli: 
    cd mydb_exporter

3. Create a virtual environment (optional but recommended):
    cli:
    virtualenv venv

4. Activate the virtual environment:
    cli:
    venv\Scripts\activate

5. Install dependencies:
    cli:
    pip install -r requirements.txt

6. Open the settings/config.ini file and Update the MySQL database connection settings:
    [database]
    host = your_database_host
    user = your_database_user
    password = your_database_password
    database = your_database_name


## Usage

1. Make sure the virtual environment is activated (if used).

2. Run the application:

python src/main.py

3. The application window will appear, displaying a list of tables from the configured MySQL database.

4. Select tables by ticking the checkbox in the first column.

5. Click the "Save" button to export the selected tables to CSV files in the working directory.
