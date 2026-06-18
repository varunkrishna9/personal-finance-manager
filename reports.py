def total_expenses(expenses):

    return sum(
        expense.amount
        for expense in expenses
    )


def average_expense(expenses):

    if len(expenses) == 0:
        return 0

    return (
        total_expenses(expenses)
        / len(expenses)
    )


def category_summary(expenses):

    summary = {}

    for expense in expenses:

        if expense.category not in summary:
            summary[expense.category] = 0

        summary[expense.category] += expense.amount

    return summary