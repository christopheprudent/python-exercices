import pandas as pd

FILE_CSV='/home/christophe/Téléchargements/titanic.csv'
df = pd.read_csv(FILE_CSV)
print(df)

# fare            (-0.001, 14.454]                     (14.454, 512.329]                    
# pclass                         1         2         3                 1         2         3
# sex    age                                                                                
# female (0, 10]               NaN       NaN  0.800000          0.000000  1.000000  0.411765
#        (10, 30]              NaN  0.933333  0.568182          0.970588  0.904762  0.307692
#        (30, 60]              NaN  0.846154  0.142857          0.979167  0.941176  0.333333
#        (60, 80]              NaN       NaN  1.000000          1.000000       NaN       NaN
# male   (0, 10]               NaN       NaN  1.000000          1.000000  1.000000  0.263158
#        (10, 30]              NaN  0.034483  0.140625          0.458333  0.000000  0.130435
#        (30, 60]              0.0  0.130435  0.109375          0.440678  0.047619  0.166667
#        (60, 80]              NaN  0.333333  0.000000          0.083333       NaN       NaN

# w/ 2 quantiles (q=2)
fare = pd.qcut(df['fare'], 2)
# array of quantiles, e.g. [0, 10, 30, 60, 80] for quartiles
age = pd.cut(df['age'], [0, 10, 30, 60, 80])

result = df.pivot_table('survived', index=['sex', age], columns=[fare, 'pclass'])
print(result)
