import pandas as pd
import numpy as np

FILE_EXCEL='/home/christophe/Téléchargements/SaleData.xlsx'

df = pd.read_excel(FILE_EXCEL)
print(df)

# eval sum on numeric columns, grouped by 'index' values
#
#                 Sale_amt  Unit_price  Units
#Region  Manager                             
#Central Douglas  124016.0      1823.0  156.0
#        Hermann  365108.5      5953.0  647.0
#        Martha   199690.0      4094.0  183.0
#        Timothy  140955.0      3621.0  213.0
#East    Douglas   48204.0       783.5  170.0
#        Martha   272803.0      4963.0  521.0
#West    Douglas   66836.0      1698.0   89.0
#        Timothy   88063.0      2048.0  142.0

result = pd.pivot_table(df, index=["Region","Manager"], aggfunc=np.sum)
print(result)

# only sale amounts
result = pd.pivot_table(df, index=["Region","Manager"], values=["Sale_amt"], aggfunc=np.sum)
print(result)
