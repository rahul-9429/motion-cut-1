import json
import os
from collections import defaultdict

 
FILE_NAME = "expenses.json"


 
def load_expense_data():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


 
def save_expense_data(expenses):
    with open(FILE_NAME, 'w') as file:
        json.dump(expenses, file, indent=4)


 
def add_expense(expenses):
    print("\nEnter details for the new expense:")
    category = input("Enter expense category: ")
    while not category:
        print("Category cannot be empty.")
        category = input("Enter expense category: ")

    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    description = input("Enter expense description: ")
    expenses.append({"category": category, "amount": amount, "description": description})
    save_expense_data(expenses)
    print("Expense added successfully!")


 
def generate_summary(expenses):
    total_expenses = sum(expense["amount"] for expense in expenses)
    category_summary = defaultdict(float)
    for expense in expenses:
        category_summary[expense["category"]] += expense["amount"]
    return total_expenses, category_summary


 
def display_summary(total_expenses, category_summary):
    print("\nExpense Summary:")
    print("Total Expenses:", total_expenses)
    print("Category-wise Summary:")
    for category, amount in category_summary.items():
        print(f"{category}: {amount}")


 
def main():
    expenses = load_expense_data()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            total_expenses, category_summary = generate_summary(expenses)
            display_summary(total_expenses, category_summary)

        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
