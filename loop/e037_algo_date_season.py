import datetime

now = datetime.date.today()
dates_season = {
    'printemps' : {
        'start' : datetime.date(now.year, 3, 20)
      , 'stop' : datetime.date(now.year, 6, 20)
    }
  , 'été' : {
        'start' : datetime.date(now.year, 6, 21)
      , 'stop' : datetime.date(now.year, 9, 21)
    }
  , 'automne' : {
        'start' : datetime.date(now.year, 9, 22)
      , 'stop' : datetime.date(now.year, 12, 20)
    }
  , 'hiver' : {
        'start' : datetime.date(now.year, 12, 21)
      , 'stop' : datetime.date(now.year +1, 3, 19)
    }
}

print('déterminer la saison correspondant à la date saisie')
mois = int(input('entrez le mois : ').strip())
jour = int(input('entrez le jour : ').strip())

date = datetime.date(now.year, mois, jour)
for s in dates_season.keys():
    if date >= dates_season[s]['start'] and date <= dates_season[s]['stop']:
        print('la saison est : %s' % s)
        break

