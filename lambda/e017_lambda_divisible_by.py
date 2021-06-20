L = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print('liste', L)
print('divisible par 19 ou par 30', list(filter(lambda x: x%19==0 or x%13==0, L)))
