# https://stackoverflow.com/questions/546321/how-do-i-calculate-the-date-six-months-from-the-current-date-using-the-datetime
import datetime
import calendar

def add_months(date, months):
    months_count = date.month + months

    # Calculate the year
    year = date.year + int(months_count / 12)

    # Calculate the month
    month = (months_count % 12)
    if month == 0:
        month = 12

    # Calculate the day
    day = date.day
    last_day_of_month = calendar.monthrange(year, month)[1]
    if day > last_day_of_month:
        day = last_day_of_month

    new_date = datetime.date(year, month, day)
    return new_date

if __name__ == "__main__":
    date = datetime.date(2018, 11, 30)

    print(date, '+  1 mois', add_months(date, 1))
    print(date, '+  3 mois', add_months(date, 3))
    print(date, '+ 14 mois', add_months(date, 14))
