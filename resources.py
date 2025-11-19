#!/usr/bin/python3

import mysql.connector

# ---- Connect to database ----
conn = mysql.connector.connect(
    host="localhost",
    user="health",
    password="Private123!",
    database="privacy_ascent"
)
cursor = conn.cursor(dictionary=True)


# ---- Resources Menu ----
def resources_menu():
    """Browse mental health resources by category."""
    print("\n----- MENTAL HEALTH RESOURCES -----")
    
    # Fetch categories
    cursor.execute("SELECT DISTINCT category FROM resources ORDER BY category")
    categories = cursor.fetchall()
    
    if not categories:
        print("\nNo resources available.")
        input("\nPress Enter to return...")
        return
    
    # Display categories
    print("\nWhat category do you need?")
    for idx, cat in enumerate(categories):
        print(f"{idx + 1}. {cat['category']}")
    
    # Get user choice
    choice = input("\nEnter category number: ").strip()
    
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(categories):
        print("\n----- Invalid choice -----")
        return
    
    # Query resources for selected category
    selected_category = categories[int(choice) - 1]['category']
    cursor.execute(
        "SELECT title, content FROM resources WHERE category = %s",
        (selected_category,)
    )
    resources = cursor.fetchall()
    
    # Display resources
    print(f"\n----- {selected_category.upper()} -----\n")
    for resource in resources:
        print(f"• {resource['title']}")
        print(f"  {resource['content']}\n")
    
    input("Press Enter to continue...")


# ---- Main Entry Point (for testing) ----
if __name__ == "__main__":
    try:
        resources_menu()
    finally:
        if conn:
            conn.close()
