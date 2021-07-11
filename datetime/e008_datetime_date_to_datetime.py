# web solution
from datetime import date
from datetime import datetime
dt = date.today()
print('date:', dt)
print('datetime:', datetime.combine(dt, datetime.min.time()))
