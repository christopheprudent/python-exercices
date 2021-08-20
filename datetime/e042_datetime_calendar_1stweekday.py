import calendar

# début semaine= Dimanche
cal = calendar.TextCalendar(calendar.SUNDAY)
cal.prmonth(2021, 8)

# début semaine= Lundi
cal.setfirstweekday(calendar.MONDAY)
cal.prmonth(2021, 8)
