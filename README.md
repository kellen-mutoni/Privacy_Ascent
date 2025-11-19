# PRIVACY ASCENT – Mental Health Navigator (Python CLI App)

A lightweight offline mental-health assistant built with Python + MySQL.

## Overview

Privacy Ascent is a command-line-based, minimal menu-driven application designed to help users monitor, understand, and seek help for their mental well-being. 

It allows users to create accounts, monitor their state of mind, find nearby clinics in Rwanda, and access emergency contacts — all offline.

The system stores all data on a personal MySQL server.
It is simple, fast, and fully accessible via the terminal.

## Key Features

- User Accounts
- Access to resources to understand mental well-being
- Recording and Monitoring State of Mind 
- Anonymous reporting of abuse cases
- Guest mode available (for accessing resources)

## Requirements

- Python 3.12.3
- MySQL server installed and functional
- mysql-connector-python (Python package)

## How to Run

### Clone or download the project folder
```
git clone https://github.com/kellen-mutoni/Privacy_Ascent.git
cd Privacy_Ascent
```

### Ensure MySQL Server Is Running
Before running database.py, confirm that your MySQL server is actually running. If MySQL is stopped, the script will fail with connection errors.

#### Linux/Mac:
```
sudo service mysql status
```

If it's not active, run: 
```
sudo service mysql start
```

#### Windows:
1. Press Win + R, type services.msc
2. Find MySQL or MySQL80
3. Make sure the status is Running
4. Start it if necessary

### Create the Project User

Log in as root and create the expected user:
```
mysql -u root -p
# Enter password to root MySQL
CREATE USER 'health'@'localhost' IDENTIFIED BY 'Private123!';
FLUSH PRIVILEGES;
GRANT ALL PRIVILEGES ON privacy_ascent.* TO 'health'@'localhost';
``` 
### Create the Project Database

Run the `database.py` script **once** to create the `privacy_ascent` database and all required tables on your MySQL server:
```
python3 database.py  # Linux / Mac
python database.py   # Windows
```
*Running it again will throw errors because tables already exist.*

## Run the Application
```
python3 main.py  # Linux / Mac
python main.py   # Windows
```