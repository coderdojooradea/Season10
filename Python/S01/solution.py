
# Capstone Project: Personal Expense Tracker

expenses = []

def add_expense():
    amount = float(input("Enter the amount: "))
    while amount <= 0:
        print("Please enter a valid amount.")
        amount = float(input("Enter the amount: "))

    category = input("Enter the category (e.g., food, transport, entertainment): ").lower()
    while category not in ['food', 'transport', 'entertainment']:
        print("Please enter a valid category.")
        category = input("Enter the category: ").lower()

    description = input("Enter a brief description: ")

    expense = {
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)
    print("Expense added successfully!")

def view_all_expenses():
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. Amount: {expense['amount']}, Category: {expense['category'].capitalize()}, Description: {expense['description']}")

def search_by_category():
    category = input("Enter the category to search for: ").lower()
    for expense in expenses:
        if expense['category'] == category:
            print(f"Amount: {expense['amount']}, Description: {expense['description']}")

def total_expenditure():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenditure: {total}")

def delete_expense():
    view_all_expenses()
    idx = int(input("Enter the number of the expense you want to delete: "))
    if 0 < idx <= len(expenses):
        del expenses[idx-1]
        print("Expense deleted successfully!")
    else:
        print("Invalid choice!")

def main_menu():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Total Expenditure")
        print("5. Delete an Expense")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            search_by_category()
        elif choice == '4':
            total_expenditure()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            print("Thank you for using the Personal Expense Tracker!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()
