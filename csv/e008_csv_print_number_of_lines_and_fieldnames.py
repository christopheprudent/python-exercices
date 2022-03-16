# web solution
import csv
fields = []
rows = []
with open('departments.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    # Following command skips the first row of the CSV file.
    fields = next(data)
    for row in data:
        print(', '.join(row))

print("\nTotal no. of rows: %d"%(data.line_num))
print('Field names are: [%s]' % ', '.join(field for field in fields))
