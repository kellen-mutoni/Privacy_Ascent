---
description: Quick start guide for Privacy Ascent
---

# Quick Start Guide

Follow these steps to get Privacy Ascent running quickly.

## First Time Setup

### 1. Install Dependencies
```bash
pip install mysql-connector-python
```

### 2. Start MySQL Service
```powershell
# Check if MySQL is running
Get-Service -Name MySQL* | Select-Object Name, Status

# Start MySQL if needed (run as Administrator)
Start-Service -Name MySQL80
```

### 3. Create Database User
```bash
mysql -u root -p
```

Then run:
```sql
CREATE USER 'health'@'localhost' IDENTIFIED BY 'Private123!';
GRANT ALL PRIVILEGES ON privacy_ascent.* TO 'health'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 4. Initialize Database (Run Once)
```bash
python database.py
```

## Running the Application

Every time you want to use Privacy Ascent:

### 1. Ensure MySQL is Running
```powershell
Get-Service -Name MySQL*
```

If not running:
```powershell
Start-Service -Name MySQL80
```

### 2. Run the Application
```bash
python main.py
```

## Common Commands

| Task | Command |
|------|---------|
| Check MySQL status | `Get-Service -Name MySQL*` |
| Start MySQL | `Start-Service -Name MySQL80` |
| Stop MySQL | `Stop-Service -Name MySQL80` |
| Connect to database | `mysql -u health -p` (password: `Private123!`) |
| Run application | `python main.py` |
| Install dependencies | `pip install mysql-connector-python` |
