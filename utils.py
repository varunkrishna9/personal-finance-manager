from datetime import datetime


def validate_amount(amount):

    try:

        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except:
        return False


def validate_date(date):

    try:

        datetime.strptime(
            date,
            "%Y-%m-%d"
        )

        return True

    except:
        return False