#!/usr/bin/python3

import mysql.connector
from datetime import datetime, timedelta

# ---- Connect to your database ----
conn = mysql.connector.connect(
    host="localhost",
    user="health",
    password="Private123!",
    database="privacy_ascent"
)
cursor = conn.cursor(dictionary=True)

# ---- Record mood function ----
def record_mood(user_id, mood_rating, notes=""):
    # Record a user's mood for the current date/time.
    try:
        cursor.execute(
            "INSERT INTO mood_tracking (user_id, mood_rating, notes) VALUES (%s, %s, %s)",
            (user_id, mood_rating, notes)
        )
        conn.commit()
        print(f"\n----- Mood recorded successfully! (Rating: {mood_rating}/10) -----\n")
    except mysql.connector.Error as err:
        print(f"----- Error recording mood: {err} -----")

# ---- Get user's mood history ----
def get_mood_history(user_id, days=30):
    # Retrieve a user's mood history for the specified number of days.
    try:
        cursor.execute(
            """
            SELECT mood_id, date, mood_rating, notes 
            FROM mood_tracking 
            WHERE user_id = %s 
            AND date >= DATE_SUB(NOW(), INTERVAL %s DAY)
            ORDER BY date DESC
            """,
            (user_id, days)
        )
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"----- Error retrieving mood history: {err} -----")
        return []

def calculate_average_mood(user_id, days=7):
    try:
        cursor.execute(
            """
            SELECT AVG(mood_rating) as avg_mood 
            FROM mood_tracking 
            WHERE user_id = %s 
            AND date >= DATE_SUB(NOW(), INTERVAL %s DAY)
            """,
            (user_id, days)
        )
        result = cursor.fetchone()
        return result['avg_mood'] if result['avg_mood'] else None
    except mysql.connector.Error as err:
        print(f"----- Error calculating average mood: {err} -----")
        return None

def analyze_mood_improvement(user_id):
    try:
        # Get average for last 7 days
        recent_avg = calculate_average_mood(user_id, days=7)
        
        # Get average for previous 7 days (8-14 days ago)
        cursor.execute(
            """
            SELECT AVG(mood_rating) as avg_mood 
            FROM mood_tracking 
            WHERE user_id = %s 
            AND date >= DATE_SUB(NOW(), INTERVAL 14 DAY)
            AND date < DATE_SUB(NOW(), INTERVAL 7 DAY)
            """,
            (user_id,)
        )
        result = cursor.fetchone()
        previous_avg = result['avg_mood'] if result['avg_mood'] else None
        
        if recent_avg is None:
            return {
                'status': 'insufficient_data',
                'message': 'Not enough recent mood data (last 7 days)'
            }
        
        if previous_avg is None:
            return {
                'status': 'no_comparison',
                'recent_average': round(recent_avg, 2),
                'message': 'No data from previous period for comparison'
            }
        
        # Calculate improvement
        improvement = recent_avg - previous_avg
        improvement_percent = (improvement / previous_avg) * 100 if previous_avg > 0 else 0
        
        # Determine trend
        if improvement > 0.5:
            trend = "improving"
        elif improvement < -0.5:
            trend = "declining"
        else:
            trend = "stable"
        
        return {
            'status': 'success',
            'recent_average': round(recent_avg, 2),
            'previous_average': round(previous_avg, 2),
            'improvement': round(improvement, 2),
            'improvement_percent': round(improvement_percent, 2),
            'trend': trend
        }
    except mysql.connector.Error as err:
        print(f"----- Error analyzing mood improvement: {err} -----")
        return {'status': 'error', 'message': str(err)}

def display_mood_analytics(user_id):
    print("\n----- Mood Analytics -----\n")
    analysis = analyze_mood_improvement(user_id)
    
    if analysis['status'] == 'success':
        print(f"Recent Average (Last 7 days): {analysis['recent_average']}/10")
        print(f"Previous Average (Days 8-14): {analysis['previous_average']}/10")
        print(f"Trend: {analysis['trend'].upper()}")
        
        if analysis['trend'] == 'improving':
            print(f"Great job! Your mood has improved by {analysis['improvement_percent']}%")
        elif analysis['trend'] == 'declining':
            print(f"Your mood has dipped slightly ({analysis['improvement_percent']}%). Consider checking out our resources.")
        else:
            print("Your mood has been relatively stable.")
            
    elif analysis['status'] == 'no_comparison':
        print(f"Recent Average (Last 7 days): {analysis['recent_average']}/10")
        print(f"Note: {analysis['message']}")
        
    else:
        print(f"Status: {analysis['message']}")

# ---- Interactive mood tracking menu ----
def mood_tracker_menu(user_id, username):
    # Interactive menu for mood tracking features.
    while True:
        print(f"\n----- Mood Tracker - Welcome, {username}! -----\n")
        print("1. Record today's mood")
        print("2. View mood analytics")
        print("3. View mood history")
        print("4. Back to main menu")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
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
            # View analytics
            display_mood_analytics(user_id)
        
        elif choice == "3":
            # View history
            print("\n----- Your Mood History -----\n")
            days = input("How many days back? (default: 30): ").strip()
            days = int(days) if days.isdigit() else 30
            
            history = get_mood_history(user_id, days)
            if history:
                print(f"\nShowing {len(history)} mood entries from the last {days} days:\n")
                for entry in history:
                    date_str = entry['date'].strftime("%Y-%m-%d %H:%M")
                    print(f"Date: {date_str}")
                    print(f"Mood: {entry['mood_rating']}/10")
                    if entry['notes']:
                        print(f"Notes: {entry['notes']}")
                    print("-" * 40)
            else:
                print(f"\nNo mood entries found in the last {days} days.")
        
        elif choice == "4":
            print("\n----- Returning to main menu... -----\n")
            break
        
        else:
            print("\n----- Invalid choice. Please try again. -----\n")