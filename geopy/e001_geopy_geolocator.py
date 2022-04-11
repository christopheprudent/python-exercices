# web solution
from functools import partial
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

ADDRESSES = [
      '27488 Stanford Avenue, North Dakota'
    , '380 New York St, Redlands, CA 92373'
    , '1600 Pennsylvania Avenue NW'
    , 'Le Maine Dufour 17360 Saint-Aigulin, France'
]

geocode = partial(geolocator.geocode, language='fr')

for addr in ADDRESSES:
    print("adresse:", addr)
    location = geocode(addr)
    print("adresse trouvée:")
    print(location.raw)
    print(location.address)
    print("géolocalisation XY:")
    print((location.latitude, location.longitude))
