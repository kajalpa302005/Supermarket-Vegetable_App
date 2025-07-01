import json
import os

DB_FILE = "vegetables.json"

def load_vegetables():
    """Load vegetables from a JSON file or create a new one if not found."""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            return json.load(file)
    else:
        print("Database not found. Creating a new one...")
        default_data = {
            "Leafy": ["Spinach", "Lettuce", "Cabbage", "Fenugreek"],
            "Ground": ["Potato", "Carrot", "Onion", "Radish"],
            "Iron-rich": ["Spinach", "Broccoli", "Beetroot", "Kale"]
        }
        with open(DB_FILE, "w") as file:
            json.dump(default_data, file, indent=4)
        return default_data

def show_menu():
    """Display the main menu to the user."""
    print("\n🥬 Welcome to the Smart Supermarket Vegetable App! 🥕")
    print("Choose an option:")
    print("1. View by Category")
    print("2. Search Vegetable")
    print("3. Add Vegetable to Category")
    print("4. Exit")

def show_categories(data):
    """Display vegetables by category."""
    print("\nAvailable Categories:")
    for category in data:
        print(f"- {category}")
    
    selected = input("Enter a category name to view vegetables: ").strip()
    if selected in data:
        print(f"\n{selected} Vegetables:")
        for veg in data[selected]:
            print(f"✅ {veg}")
    else:
        print("❌ Category not found!")

def search_vegetable(data):
    """Search for a vegetable in all categories."""
    query = input("Enter vegetable name to search: ").strip().lower()
    found = False
    for category, vegetables in data.items():
        for veg in vegetables:
            if query == veg.lower():
                print(f"✅ {veg} found in category '{category}'")
                found = True
    if not found:
        print("❌ Vegetable not found.")

def add_vegetable(data):
    """Add a new vegetable to an existing category."""
    category = input("Enter category to add vegetable to: ").strip()
    if category not in data:
        print("❌ Category doesn't exist.")
        return
    veg = input("Enter vegetable name to add: ").strip()
    if veg in data[category]:
        print("❗ This vegetable already exists in the category.")
    else:
        data[category].append(veg)
        with open(DB_FILE, "w") as file:
            json.dump(data, file, indent=4)
        print(f"✅ {veg} added to {category}.")

def main():
    data = load_vegetables()
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                show_categories(data)
            elif choice == 2:
                search_vegetable(data)
            elif choice == 3:
                add_vegetable(data)
            elif choice == 4:
                print("👋 Thank you for using the app!")
                break
            else:
                print("❌ Invalid choice. Please enter a number from 1 to 4.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
