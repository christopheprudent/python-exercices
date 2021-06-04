import enum

# web solution
class Countries(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    India = 355
    USA = 213

for result in Countries:
    print('{:>15} = {:3d}'.format(result.name, result.value))

