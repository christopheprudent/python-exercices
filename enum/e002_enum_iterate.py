import enum

# web solution
class Country(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

for data in Country:
    print('{:>15} = {:3d}'.format(data.name, data.value))
