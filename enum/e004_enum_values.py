import enum

# web solution
class Country(enum.IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

country_code_list = list(map(int, Country))
print(sorted(country_code_list))
