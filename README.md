# Expense Tracker (Python Mini Project)

A beginner-friendly command-line app to track daily spending. Built for Module 2 (Python Mini Project) of my internship.

## Features

- Add expenses with description, category, and amount (date is added automatically)
- View all expenses in a neat table with a running total
- See spending totals and percentages by category
- Delete a wrong entry
- Data is saved automatically to `expenses.json`, so nothing is lost when you close the program
- Input validation: bad numbers or menu choices don't crash the app

## How to run

1. Install Python 3 from https://www.python.org/downloads/
2. Open a terminal in this folder
3. Run:
   ```
   python expense_tracker.py
   ```

## Sample output

```
=== Expense Tracker ===
1. Add expense
2. View all expenses
3. Summary by category
4. Delete an expense
5. Exit

Spending by category:
  Food       Rs    320.00  (64%)
  Travel     Rs    180.00  (36%)
```

## Python concepts used

- Functions, loops (`while`, `for`), and conditionals
- Lists and dictionaries
- File handling and the `json` module
- Exception handling (`try / except`)
- The `datetime` module and f-string formatting

## Ideas for future improvement

- Filter expenses by month
- Set a monthly budget with a warning
- Export to CSV or draw a chart

## Author

Aakash Singh
