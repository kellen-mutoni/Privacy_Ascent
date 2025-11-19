# RUN ONCE
import mysql.connector


def create_database():
        # Connect to MySQL server (adjust user/password as needed)
        conn = mysql.connector.connect(
            host="localhost",
            user="health",
            password="Private123!"
        )
        cursor = conn.cursor()

        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS privacy_ascent")
        cursor.execute("USE privacy_ascent")

        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                age INT,
                gender VARCHAR(10)
            )
        """)

        # Cases table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cases (
                case_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                case_type VARCHAR(75) NOT NULL,
                description TEXT,
                anonymous BOOLEAN DEFAULT FALSE,
                date_reported DATETIME DEFAULT CURRENT_TIMESTAMP,
                location VARCHAR(255) NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)

        # Resources table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS resources (
                resource_id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                category VARCHAR(75) NOT NULL,
                content TEXT
            )
        """)

        # Mood tracking table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mood_tracking (
                mood_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                date DATETIME DEFAULT CURRENT_TIMESTAMP,
                mood_rating INTEGER,
                notes TEXT,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)

        conn.commit()
        print("----- MySQL Database created successfully! -----")


create_database()

