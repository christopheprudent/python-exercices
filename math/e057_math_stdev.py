# web solution
import math
import sys

def sd_calc(data):
    n = len(data)

    if n <= 1:
        return 0.0

    mean, sd = avg_calc(data), 0.0
    print('n={0} mean={1:f}'.format(n, mean))

    # calculate stan. dev.
    for el in data:
        sd += (float(el) - mean)**2

    # list: n éléments, de 0 à n-1 ?
    # formule : RACINE(1/n * SOMME(1, n):(Xi - Xm)**2)
    sd = math.sqrt(sd / float(n-1))

    return sd

def avg_calc(ls):
    n, mean = len(ls), 0.0

    if n <= 1:
        return ls[0]

    # calculate average
    for el in ls:
        mean = mean + float(el)
    mean = mean / float(n)

    return mean

data = [4, 2, 5, 8, 6]
print("Sample Data: ",data)
print("Standard Deviation : ", sd_calc(data))

import statistics
print("Standard Deviation : ", statistics.stdev(data))

