# web solution
import csv
with open('temp2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(('id1', 'id2', 'date'))
    for i in range(3):
        row = (
            i + 1,
            chr(ord('a') + i),
            '01/{:02d}/2022'.format(i + 1),)
        writer.writerow(row)

print(open('temp2.csv', 'r').read())
