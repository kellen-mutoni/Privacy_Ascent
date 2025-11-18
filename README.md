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
- MySQL connector

## How to Run

### Clone or download the project folder
```
git clone https://github.com/kellen-mutoni/Privacy_Ascent.git
```

### Create the Project User

You have to create the MySQL login user that your script expects, by running the command below:

```
CREATE USER 'health'@'localhost' IDENTIFIED BY 'Private123!';
GRANT ALL PRIVILEGES ON privacy_ascent.* TO 'health'@'localhost';
FLUSH PRIVILEGES;
``` 
### Create the Project Database

Run the database.py script **once** to create the database and all required tables on your MySQL server:
```
python3 database.py  # Linux / Mac
python database.py   # Windows
```

## Run the Application
```
python3 main.py  # Linux / Mac
python main.py   # Windows
```

