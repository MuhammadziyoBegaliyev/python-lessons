import datetime


def print_next_14_days():
    today = datetime.date.today()

    next_14_days = [today + datetime.timedelta(days=i) for i in range(14)]

    for day in next_14_days:
        print(day)


print_next_14_days()
