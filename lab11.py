import datetime
import json

EXPENSE_FILE = "expenses.json"

expenses = []

def load_expenses():
    """Loads expenses from the JSON file."""
    try:
        with open(EXPENSE_FILE, 'r') as f:
            global expenses
            data = json.load(f)
            # Convert date strings back to datetime.date objects after loading
            expenses = [{"date": datetime.datetime.strptime(exp['date'], '%Y-%m-%d').date(),
                         "category": exp['category'],
                         "amount": exp['amount'],
                         "description": exp['description']} for exp in data]
    except FileNotFoundError:
        pass
    print("Expenses loaded (if any).\n")

def save_expenses():
    """Saves expenses to the JSON file."""
    with open(EXPENSE_FILE, 'w') as f:
        # Convert datetime.date objects to strings before saving
        data = [{"date": exp['date'].strftime('%Y-%m-%d'),
                 "category": exp['category'],
                 "amount": exp['amount'],
                 "description": exp['description']} for exp in expenses]
        json.dump(data, f, indent=4) # Added indent for better readability of the JSON file

def add_expense():
    """Adds a new expense."""
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    category = input("Enter category: ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount >= 0:
                break
            else:
                print("Amount must be non-negative.")
        except ValueError:
            print("Invalid amount. Please enter a number.")
    description = input("Enter description: ")
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })
    save_expenses()
    print("Expense added and saved.\n")

def view_expenses():
    """Displays all recorded expenses."""
    if not expenses:
        print("No expenses recorded.\n")
        return
    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date'].strftime('%Y-%m-%d')} | {exp['category']} | ${exp['amount']:.2f} | {exp['description']}")
    print("--------------------\n")

def total_by_category():
    """Calculates and displays the total expenses for a given category."""
    category = input("Enter category: ")
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == category.lower())
    print(f"Total spent on {category}: ${total:.2f}\n")

def delete_expense():
    """Deletes an expense based on its number in the displayed list."""
    if not expenses:
        print("No expenses recorded. Nothing to delete.\n")
        return
    view_expenses()
    while True:
        try:
            idx_to_delete = int(input("Enter the number of the expense to delete: "))
            if 1 <= idx_to_delete <= len(expenses):
                deleted_expense = expenses.pop(idx_to_delete - 1)
                save_expenses()
                print(f"Expense '{deleted_expense['description']}' deleted and changes saved.\n")
                break
            else:
                print("Invalid expense number. Please choose a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def menu():
    """Displays the main menu and handles user choices."""
    load_expenses() # Load expenses when the program starts
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total by Category")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    menu()
