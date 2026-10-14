"""Expense Tracker - a simple command-line app to record and review spending.

Features: add expenses, view all, total by category, delete, and automatic
saving to a JSON file so your data is still there next time.
"""

import json
from datetime import date

DATA_FILE = "expenses.json"


def load_expenses():
    """Read saved expenses from the file (empty list if none yet)."""
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    """Write the expenses list to the file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def get_amount():
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            amount = float(input("Amount: "))
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a number, e.g. 250 or 99.5")


def add_expense(expenses):
    description = input("Description (e.g. Lunch): ").strip() or "Misc"
    category = input("Category (Food/Travel/Bills/Fun/Other): ").strip().title() or "Other"
    amount = get_amount()
    expenses.append({
        "date": str(date.today()),
        "description": description,
        "category": category,
        "amount": amount,
    })
    save_expenses(expenses)
    print(f"Added: {description} - Rs {amount:.2f} [{category}]")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(f"\n{'No.':<4}{'Date':<12}{'Description':<20}{'Category':<10}{'Amount':>10}")
    print("-" * 56)
    for i, e in enumerate(expenses, start=1):
        print(f"{i:<4}{e['date']:<12}{e['description'][:18]:<20}"
              f"{e['category']:<10}{e['amount']:>10.2f}")
    print("-" * 56)
    print(f"{'Total':<46}{sum(e['amount'] for e in expenses):>10.2f}")


def summary_by_category(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    grand_total = sum(totals.values())
    print("\nSpending by category:")
    for cat, amt in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<10} Rs {amt:>9.2f}  ({amt / grand_total * 100:.0f}%)")


def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        num = int(input("Enter the number to delete: "))
        removed = expenses.pop(num - 1)
        save_expenses(expenses)
        print(f"Deleted: {removed['description']}")
    except (ValueError, IndexError):
        print("Invalid number.")


def main():
    expenses = load_expenses()
    menu = """
=== Expense Tracker ===
1. Add expense
2. View all expenses
3. Summary by category
4. Delete an expense
5. Exit"""
    while True:
        print(menu)
        choice = input("Choose (1-5): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary_by_category(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Goodbye! Your data is saved.")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
