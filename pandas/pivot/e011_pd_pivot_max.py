import pandas as pd
import numpy as np

FILE_EXCEL='/home/christophe/Téléchargements/SaleData.xlsx'

df = pd.read_excel(FILE_EXCEL)
print(df)

table = pd.pivot_table(df,index=["Item"], values="Sale_amt", aggfunc=max)
print(table)
