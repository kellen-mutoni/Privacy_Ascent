#!/usr/bin/python3

auth = __import__('auth').auth
mood_tracker_menu = __import__('mood').mood_tracker_menu
resources_menu = __import__('resources').resources_menu

logged_in = False

# ---- Welcome Screen ----
def welcome_screen():
    print("WELCOME TO PRIVACY ASCENT")
    print("Mental Health Navigator\n")
    print("\nYour safe space to monitor your mental well-being")

# ---- Main Menu (After Login) ----
def main_menu(username, user_id):
    """Main menu displayed after successful login."""
    while True:
        print("\n" *10)
        print(f"MAIN MENU - Welcome, {username}!")
        print("\n1. Mood Tracker")
        print("2. Mental Health Resources")
        print("3. Report Abuse Case")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        # Mood Tracker
        if choice == "1":
            mood_tracker_menu(user_id, username)
        
        # Mental Health Resources
        elif choice == "2":
            resources_menu()
        
        # Report Abuse Case
        elif choice == "3":
            print("\n----- Report Abuse Case -----")
            print("This feature is coming soon!")
            print("You'll be able to report abuse cases anonymously.")
            input("\nPress Enter to continue...")
        
        # Exit
        elif choice == "4":
            print(f"\n----- Goodbye, {username}! Take care of yourself. -----\n")
            break
        
        else:
            print("\n----- Invalid choice. Please try again. -----")


# ---- Guest Menu ----
def guest_menu():
    while True:
        print("\nGUEST MODE\n")
        print("\n1. View Mental Health Resources")
        print("2. Create Account/ Log in")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            resources_menu()
        
        elif choice == "2":
            auth()
            
        elif choice == "3":
            print("\n----- Thank you for visiting Privacy Ascent. Stay well! -----\n")
            break
        
        else:
            print("\n----- Invalid choice. Please try again. -----")


# ---- Start Menu ----
def main():
    while True:
        welcome_screen()
        print("\n" *2)
        print("What would you like to do today?")
        print("1. Sign In")
        print("2. Continue as Guest")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            user = auth()
            if user:
                logged_in = True
                main_menu(user['username'], user['user_id'])
        elif choice == "2":
            guest_menu()
        elif choice == "3":
            print("\n----- Thank you for using Privacy Ascent. Take care! -----")
            break
        else:
            print("\n----- Invalid choice. Please try again. -----")

main()