# GaragePro CLI

GaragePro is a command-line Python application for managing vehicle service records in an auto garage. It uses SQLAlchemy for ORM, Alembic for migrations, and Click for CLI interactions.

## 🚀 Features

- Register customers and their vehicles
- Log service records with cost and notes
- View service history for any vehicle
- Built-in CLI interface using Click
- SQLite database with Alembic migrations

---

## Tech Stack
- Python
- SQLAlchemy
- Alembic
- Click
- SQLite

## Setup
1. Clone the repo
2. Create a virtual environment
3. Install dependencies
4. Run Alembic migrations

## 🗂️ Project Structure
garagepro-cli/ 
├── cli.py  
├── database.py        
├── main.py             
├── models.py           
├── migrations/       
├── alembic.ini        
├── garagepro.db        
└── README.md           

---

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd garagepro-cli
   python -m venv venv
   pip install sqlalchemy alembic click
   alembic init migrations
   sqlalchemy.url = sqlite:///garagepro.db


## CLI Usage
Run the CLI via main.py:
python main.py [command]

## Available Commands:
- add-customer – Register a new customer
- add-vehicle – Add a vehicle to a customer
- log-service – Log a service record for a vehicle
- view-history – View service history for a vehicle
- filter-vehicles – Search vehicles by make/model/year

## Author
James Ivan





