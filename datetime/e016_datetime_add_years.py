# from web: https://stackoverflow.com/questions/15741618/add-one-year-in-current-date-python/15743908
from datetime import date

def add_years(d, years):
    """Return a date that's `years` years after the date (or datetime)
    object `d`. Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (thus changing February 29 to March 1).

    """
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

if __name__ == "__main__":
    print(add_years(date(2015, 1, 1), -1))
    print(add_years(date(2015, 1, 1), 0))
    print(add_years(date(2015, 1, 1), 2))
    print(add_years(date(2000, 2, 29), 1)) 
