import datetime

expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })
    print("Expense added.\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} | {exp['category']} | ${exp['amount']} | {exp['description']}")

def total_by_category():
    category = input("Enter category: ")
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == category.lower())
    print(f"Total spent on {category}: ${total:.2f}\n")

def delete_expense():
    view_expenses()
    idx = int(input("Enter the number of the expense to delete: "))
    if 1 <= idx <= len(expenses):
        del expenses[idx - 1]
        print("Expense deleted.\n")
    else:
        print("Invalid entry.\n")

def menu():
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

menu()
