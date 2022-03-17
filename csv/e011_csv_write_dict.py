# web solution
import csv
csv_columns = ['id','Column1', 'Column2', 'Column3', 'Column4', 'Column5']
dict_data = {
    'id':['1', '2', '3'],
    'Column1':[33, 25, 56],
    'Column2':[35, 30, 30],
    'Column3':[21, 40, 55],
    'Column4':[71, 25, 55],
    'Column5':[10, 10, 40], 
}

csv_file = "temp4.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        #for data in dict_data:
        #    writer.writerow(dict_data)
        for i in range(3):
            row = {
                'id':dict_data['id'][i]
                , 'Column1':dict_data['Column1'][i]
                , 'Column2':dict_data['Column2'][i]
                , 'Column3':dict_data['Column3'][i]
                , 'Column4':dict_data['Column4'][i]
                , 'Column5':dict_data['Column5'][i]
            }
            writer.writerow(row)
except IOError:
   print("I/O error")

data = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data:
    print(row)
