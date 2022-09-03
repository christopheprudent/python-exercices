import pandas as pd
import numpy as np

FILE_EXCEL='/home/christophe/Téléchargements/SaleData.xlsx'

df = pd.read_excel(FILE_EXCEL)
print(df)

# eval sum on ['Units', 'Sale_amt'] columns, grouped by ['Region', 'Manager', 'SalesMan'] values, only for Manager equal to 'Douglas'
#
#                          Sale_amt  Units
#Region  Manager SalesMan                 
#Central Douglas John      124016.0  156.0
#East    Douglas Karen      48204.0  170.0
#West    Douglas Michael    66836.0   89.0

# only sale amounts
#result = df.loc[df["Manager"]=='Douglas']
result = pd.pivot_table(df.loc[df["Manager"]=='Douglas'], index=["Region", "Manager", "SalesMan"], values=["Units", "Sale_amt"], aggfunc=np.sum)
print(result)

table = pd.pivot_table(df,index=["Region","Manager","SalesMan"], values="Sale_amt", aggfunc=np.sum)
print(table.query('Manager == ["Douglas"]'))
