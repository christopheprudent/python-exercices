"""
Write a Pandas program to create a Pivot table and find number of survivors and average rate grouped by gender and class.
"""

import pandas as pd

FILE_CSV='/home/christophe/Téléchargements/titanic.csv'
df = pd.read_csv(FILE_CSV)
print(df)

result = df.pivot_table(index=['sex', 'class'], values='survived', aggfunc=['count', 'mean'])
print(result)

# 'fare' : prix du billet
#              fare                       survived             
#class        First     Second      Third    First Second Third
#sex                                                           
#female  106.125798  21.970121  16.118810       91     70    72
#male     67.226127  19.741782  12.661633       45     17    47
result = df.pivot_table(index='sex', columns='class', aggfunc={'survived':sum, 'fare':'mean'})
print(result)
#                     fare  survived
#sex    class                       
#female First   106.125798        91
#       Second   21.970121        70
#       Third    16.118810        72
#male   First    67.226127        45
#       Second   19.741782        17
#       Third    12.661633        47
result = df.pivot_table(index=['sex', 'class'], aggfunc={'survived':sum, 'fare':'mean'})
print(result)
