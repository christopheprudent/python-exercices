# read a date (month, day) of year 2016, knowing 1/1 is Friday and 2016 is a leap year

days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']

print('Entrez le mois et le jour (m d) de l\'année 2016')
m, d = map(int, input().split())
ndays = sum(days_in_month[:m-1])
ndays += (d-1)

print('le %d/%d/2016 était un %s' %(d,m,day_of_week[ndays%7]))
