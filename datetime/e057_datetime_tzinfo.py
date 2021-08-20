# web solution
import time
import os

def zone_info():
   print('TZ   :', os.environ.get('TZ', '(not set)'))
   print('Timezone abbreviations:', time.tzname)
   print('Timezone : {} ({})'.format(
       time.timezone, (time.timezone / 3600)))
   print('DST timezone ', time.daylight)
   print('Time :', time.strftime('%X %x %Z'),'\n')

print('Default Zone:')
zone_info()

TIME_ZONES = [
   'Pacific/Auckland',
   'Europe/Berlin',
   'Europe/Paris',
   'America/Detroit',
   'Singapore',
]
for zone in TIME_ZONES:
   os.environ['TZ'] = zone
   time.tzset()
   print(zone, ':')
   zone_info()
