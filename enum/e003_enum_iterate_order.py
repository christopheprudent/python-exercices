import enum

class Country(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

for data in sorted(Country, key= lambda x:x.value):
    print('{:>15} = {:3d}'.format(data.name, data.value))

# web solution
class Country2(enum.IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

print()
for data in sorted(Country2):
    print('{:>15} = {:3d}'.format(data.name, data.value))

