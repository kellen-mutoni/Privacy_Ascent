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

# ---- Calculate average mood from previous entries ----
def get_average_mood(user_id):
    try:
        cursor.execute(
            """
            SELECT AVG(mood_rating) as avg_mood 
            FROM mood_tracking 
            WHERE user_id = %s
            """,
            (user_id,)
        )
        result = cursor.fetchone()
        return result['avg_mood'] if result['avg_mood'] else None
    except mysql.connector.Error as err:
        print(f"----- Error calculating average mood: {err} -----")
        return None

# ---- Record mood and show comparison ----
def record_mood(user_id, mood_rating, notes=""):
    try:
        avg_mood = get_average_mood(user_id)
        
        # Insert the new mood entry
        cursor.execute(
            "INSERT INTO mood_tracking (user_id, mood_rating, notes) VALUES (%s, %s, %s)",
            (user_id, mood_rating, notes)
        )
        conn.commit()
        
        print(f"\n----- Mood recorded successfully! (Rating: {mood_rating}/10) -----\n")
        
        # Show comparison with average
        if avg_mood is None:
            print("This is your first mood entry! Keep tracking to see your progress.\n")
        else:
            avg_mood = round(avg_mood, 1)
            print(f"Your average mood: {avg_mood}/10")
            print(f"Current mood: {mood_rating}/10\n")
            
            # Compare and show encouraging or supportive message
            if mood_rating >= avg_mood:
                # Current mood is at or above average - encouraging message
                print("Great news! You're doing well today!")
                print("Your mood is at or above your average. Keep up the positive energy!\n")
            else:
                # Current mood is below average - supportive message
                print("We notice you're feeling a bit down today.")
                print("Remember, it's okay to have tough days. Here are some things you can try:")
                print("  - Talk to someone you trust")
                print("  - Take a short walk or do light exercise")
                print("  - Practice deep breathing or meditation")
                print("  - Consider reaching out to a counselor or mental health professional")
                print("\nYou're not alone, and things can get better. Take care of yourself!\n")
                
    except mysql.connector.Error as err:
        print(f"----- Error recording mood: {err} -----")

# ---- Interactive mood tracking menu ----
def mood_tracker_menu(user_id, username):
    while True:
        print(f"\n----- Mood Tracker - Welcome, {username}! -----\n")
        print("1. Record your current mood")
        print("2. Back to main menu")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            # Record mood
            print("\n----- Record Your Mood -----\n")
            print("Rate your current mood on a scale of 1-10:")
            print("1-3: Very low/struggling")
            print("4-6: Moderate/okay")
            print("7-9: Good/positive")
            print("10: Excellent/amazing\n")
            
            try:
                rating = int(input("Mood rating (1-10): ").strip())
                if 1 <= rating <= 10:
                    notes = input("Add notes (optional, press Enter to skip): ").strip()
                    record_mood(user_id, rating, notes)
                else:
                    print("----- Please enter a number between 1 and 10 -----")
            except ValueError:
                print("----- Invalid input. Please enter a number -----")
        elif choice == "2":
            print("\n----- Returning to main menu... -----\n")
            break
        else:
            print("\n----- Invalid choice. Please try again. -----\n")