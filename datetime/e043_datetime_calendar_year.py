import calendar

# default: (year, w=2, l=1, c=6, m=3)
print(calendar.calendar(2021))

# year: 2021
# column width: 2
# lines per week: 1 
# number of spaces between month columns: 1
# 3: no. of months per column.
#print(calendar.calendar(2021, 2, 1, 1, 3))

# formatyear(theyear, w=2, l=1, c=6, m=3)
# Return a m-column calendar for an entire year as a multi-line string.
# Optional parameters w, l, and c are for date column width, lines per week, and number of spaces between month columns, respectively.
#cal = calendar.TextCalendar(calendar.MONDAY)
#print(cal.formatyear(2022, 2, 1, 1, 3))

#import locale
#locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
#print(calendar.calendar(2021))

cal = calendar.LocaleTextCalendar(locale='fr_FR.utf8')
cal.prmonth(2025, 9)
