#!/usr/bin/python3

import mysql.connector

# ---- Connect to your database ----
conn = mysql.connector.connect(
    host="localhost",
    user="health",
    password="Private123!",
    database="privacy_ascent"
)
cursor = conn.cursor(dictionary=True)

# ---- Register function ----
def register(username, password, age=None, gender=None):
    try:
        cursor.execute(
            "INSERT INTO users (username, password, age, gender) VALUES (%s, %s, %s, %s)",
            (username, password, age, gender)
        )
        conn.commit()
        print("Registration successful!")
    except mysql.connector.IntegrityError:
        print("Username already exists!")

# ---- Login function ----
def login(username, password):
    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )
    user = cursor.fetchone()
    if user:
        print(f"Login successful! Welcome, {user['username']}")
        return True
    print("Invalid username or password.")
    return False

# ---- Login Menu Logic ----
if __name__ == "__main__":
    while True:
        action = input("Do you have an account? [Yes/No/exit]? ").strip().lower()
        if action == "no":
            print("\n----- Create an Account: -----\n")
            uname = input("Username: ").strip()
            pwd = input("Password: ").strip()
            age = input("Age (optional): ").strip()
            gender = input("Gender (optional): ").strip()
            age = int(age) if age.isdigit() else None
            gender = gender if gender else None
            register(uname, pwd, age, gender)
        elif action == "yes":
            print("\n----- Enter your Details to Sign in -----\n")
            uname = input("Username: ").strip()
            pwd = input("Password: ").strip()
            login(uname, pwd)
        elif action == "exit":
            break
        else:
            print("Unknown command")

