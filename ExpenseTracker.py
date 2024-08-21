import json
from datetime import datetime

# Data structure to store expenses
expenses = []

# Function to add an expense
def add_expense(amount, description, category):
    expense = {
        'amount': amount,
        'description': description,
        'category': category,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    expenses.append(expense)
    print("Expense added successfully!")

# Function to save expenses to a file
def save_expenses(filename='expenses.json'):
    with open(filename, 'w') as file:
        json.dump(expenses, file)
    print("Expenses saved to file.")

# Function to load expenses from a file
def load_expenses(filename='expenses.json'):
    global expenses
    try:
        with open(filename, 'r') as file:
            expenses = json.load(file)
        print("Expenses loaded from file.")
    except FileNotFoundError:
        print("No previous expenses found. Starting fresh.")

# Function to view summary of expenses
def view_summary():
    total_expense = sum(expense['amount'] for expense in expenses)
    print(f"Total Expense: {total_expense}")
    category_summary = {}
    for expense in expenses:
        category = expense['category']
        category_summary[category] = category_summary.get(category, 0) + expense['amount']
    for category, total in category_summary.items():
        print(f"{category}: {total}")

# Function to handle user input
def user_interface():
    load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Save and Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category = input("Enter category (e.g., food, transportation, entertainment): ")
                add_expense(amount, description, category)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == '2':
            view_summary()
        elif choice == '3':
            save_expenses()
            break
        else:
            print("Invalid choice. Please try again.")

# Run the user interface
if __name__ == "__main__":
    user_interface()
