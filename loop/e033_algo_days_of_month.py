days_of_month = {
    'January' : 31
  , 'February' : [28, 29]
  , 'March' : 31
  , 'April' : 30
  , 'May' : 31
  , 'June' : 30
  , 'July' : 31
  , 'August' : 31
  , 'September' : 30
  , 'October' : 31
  , 'November' : 30
  , 'December' : 31
}

while True:
    month = input('entrez le mois (en anglais) : ').capitalize()
    if len(month) == 0:
        break
    if month in days_of_month:
        if isinstance(days_of_month[month], list):
            #print('le mois %s compte %d/%d jours' % (month, days_of_month[month][0], days_of_month[month][1]))
            print('le mois %s compte %s jours' % (month, '/'.join(map(str, days_of_month[month]))))
        else:
            print('le mois %s compte %s jours' % (month, days_of_month[month]))
