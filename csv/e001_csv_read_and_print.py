# web solution
import csv

print('en mode liste')
with open('departments.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    #print(list(data))
    for row in data:
        print(', '.join(row))

print('\nen mode dictionnaire')
with open('departments.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        print(row)
