# Cafe Management System

This project is a simple **Cafe Management System** built using **Flask**. It allows users to manage cafe items such as adding, viewing, updating, and deleting items from a SQL Server database. The system also supports user authentication using JWT (JSON Web Tokens).

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Authentication**: Secure login/logout functionality with JWT tokens.
- **CRUD Operations**: Create, update, delete, and fetch cafe menu items.
- **Data Storage**: Uses **SQL Server** as the database to store menu items.

## Tech Stack

- **Backend**: Flask, Flask-JWT-Extended
- **Database**: SQL Server
- **Authentication**: JWT (JSON Web Tokens)
- **API Design**: RESTful API

## Installation

### Prerequisites

- Python 3.x
- SQL Server
- Virtual environment (recommended)

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cafe-management-system.git
   cd cafe-management-system/backend

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate 

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

4. Configure your SQL Server connection:
   Open the config.py file and update the SQLALCHEMY_DATABASE_URI:

    ```bash
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://username:password@server/database'
    
5. Initialize the database:
    ```bash
    flask db init

6. Generate migrations:
    ```bash
    flask db migrate

7. Apply migrations to the database:
    ```bash
    flask db upgrade

8. Start the Flask development server:
    ```bash
    flask run
    
## The backend server will run on http://127.0.0.1:5000.
