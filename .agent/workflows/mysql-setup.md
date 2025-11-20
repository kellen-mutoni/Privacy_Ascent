---
description: MySQL connector setup and database initialization
---

# MySQL Connector Setup and Database Initialization

This workflow guides you through setting up the MySQL connector and initializing the Privacy Ascent database.

## Prerequisites

1. **Install Python 3.12.3 or higher**
   - Verify installation:
   ```bash
   python --version
   ```

2. **Install MySQL Server**
   - Download from: https://dev.mysql.com/downloads/mysql/
   - During installation, set a root password (remember this!)

## Step 1: Verify MySQL Server is Running

### Windows:
```powershell
# Open Services Manager
services.msc
```
- Find "MySQL" or "MySQL80" in the list
- Ensure Status shows "Running"
- If not running, right-click and select "Start"

**Alternative - Check via Command Line:**
```powershell
# Check if MySQL service is running
Get-Service -Name MySQL* | Select-Object Name, Status
```

**Start MySQL if stopped:**
```powershell
# Start MySQL service (run as Administrator)
Start-Service -Name MySQL80
```

## Step 2: Install MySQL Connector for Python

### Option A: Using pip (Recommended)
```bash
pip install mysql-connector-python
```

### Option B: Using virtual environment (Best Practice)
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1

# Windows Command Prompt:
.venv\Scripts\activate.bat

# Install mysql-connector-python
pip install mysql-connector-python
```

## Step 3: Create MySQL User for the Project

```bash
# Connect to MySQL as root
mysql -u root -p
```

When prompted, enter your MySQL root password.

**Then run these SQL commands:**
```sql
-- Create the 'health' user
CREATE USER 'health'@'localhost' IDENTIFIED BY 'Private123!';

-- Grant privileges on the privacy_ascent database
GRANT ALL PRIVILEGES ON privacy_ascent.* TO 'health'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

-- Exit MySQL
EXIT;
```

## Step 4: Initialize the Database

Run the database setup script **once** to create the database and tables:

```bash
python database.py
```

**Expected Output:**
```
----- MySQL Database created successfully! -----
```

**Note:** Running this script multiple times may cause errors if tables already exist.

## Step 5: Verify Database Creation

```bash
# Connect to MySQL
mysql -u health -p
# Password: Private123!
```

**Verify the database and tables:**
```sql
-- Show databases
SHOW DATABASES;

-- Use the privacy_ascent database
USE privacy_ascent;

-- Show all tables
SHOW TABLES;

-- Verify table structure
DESCRIBE users;
DESCRIBE mood_tracking;
DESCRIBE cases;
DESCRIBE resources;

-- Exit
EXIT;
```

## Step 6: Run the Application

```bash
python main.py
```

## Troubleshooting

### Error: "Access denied for user 'health'@'localhost'"
**Solution:** Re-run Step 3 to create the user and grant privileges.

### Error: "Can't connect to MySQL server on 'localhost'"
**Solution:** 
1. Verify MySQL service is running (Step 1)
2. Check if MySQL is listening on port 3306:
   ```powershell
   netstat -an | findstr 3306
   ```

### Error: "No module named 'mysql.connector'"
**Solution:** Install the MySQL connector (Step 2)

### Error: "Table 'users' already exists"
**Solution:** This is normal if you've already run `database.py`. You can skip Step 4.

## Quick Reference Commands

### Check MySQL Service Status
```powershell
Get-Service -Name MySQL*
```

### Start MySQL Service
```powershell
Start-Service -Name MySQL80
```

### Stop MySQL Service
```powershell
Stop-Service -Name MySQL80
```

### Connect to MySQL
```bash
mysql -u health -p
# Password: Private123!
```

### Run the Application
```bash
python main.py
```
