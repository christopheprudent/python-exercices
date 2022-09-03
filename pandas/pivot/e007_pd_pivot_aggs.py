import pandas as pd
import numpy as np

FILE_EXCEL='/home/christophe/Téléchargements/SaleData.xlsx'

df = pd.read_excel(FILE_EXCEL)
print(df)

# eval count & mean on 'Sale_amt' column, grouped by 'Manager' values
#
#                 mean      len
#             Sale_amt Sale_amt
#Manager                       
#Douglas  29882.000000        8
#Hermann  30425.708333       12
#Martha   33749.500000       14
#Timothy  25446.444444        9

# only sale amounts
result = pd.pivot_table(df, index=["Manager"], values=["Sale_amt"], aggfunc=[np.mean, len])
print(result)
