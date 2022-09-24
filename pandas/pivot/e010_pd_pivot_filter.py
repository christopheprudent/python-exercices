import pandas as pd
import numpy as np

FILE_EXCEL='/home/christophe/Téléchargements/SaleData.xlsx'

df = pd.read_excel(FILE_EXCEL)
print(df)

table = pd.pivot_table(df,index=["Region", "Item"], values="Units", aggfunc=[len, np.mean, min, max])
print(table.query('Item == ["Television","Home Theater"]'))
