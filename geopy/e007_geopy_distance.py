# Bordeaux 44° 51′ 50″ N, 0° 34′ 55″ O
# Toulouse 43° 36′ 01″ N, 1° 25′ 58″ E 

from geopy import distance
bordeaux = ("44.5150° N, 0.3455° W")
toulouse = ("43.3601° N, 1.2558° E")
print("Distance entre Bordeaux et Toulouse (en km):")
print(distance.distance(bordeaux, toulouse).km,"km")

# 181.64214026451634 km
# au lieu de 211.38 (à vol d'oiseau)
