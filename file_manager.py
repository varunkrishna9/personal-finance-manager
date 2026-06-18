import csv
import os

from src.expense import Expense

FILE_NAME = "data/expenses.csv"
def load_expenses():

    expenses = []

    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader, None)

        for row in reader:

            if len(row) == 4:

                expense = Expense(
                    row[2],
                    row[1],
                    row[0],
                    row[3]
                )

                expenses.append(expense)

    return expenses
def save_expenses(expenses):

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Date",
            "Category",
            "Amount",
            "Description"
        ])

        for expense in expenses:

            writer.writerow([
                expense.date,
                expense.category,
                expense.amount,
                expense.description
            ])