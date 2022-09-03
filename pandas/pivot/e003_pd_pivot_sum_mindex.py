import pandas as pd
import numpy as np

FILE_EXCEL='/home/christophe/Téléchargements/SaleData.xlsx'

df = pd.read_excel(FILE_EXCEL)
print(df)

# eval sum on 'Sale_amt' column, grouped by 'index' values
#
#                           Sale_amt
#Region  Manager SalesMan           
#Central Douglas John       124016.0
#        Hermann Luis       206373.0
#                Shelli      33698.0
#                Sigal      125037.5
#        Martha  Steven     199690.0
#        Timothy David      140955.0
#East    Douglas Karen       48204.0
#        Martha  Alexander  236703.0
#                Diana       36100.0
#West    Douglas Michael     66836.0
#        Timothy Stephen     88063.0

# only sale amounts
result = pd.pivot_table(df, index=["Region","Manager", "SalesMan"], values=["Sale_amt"], aggfunc=np.sum)
print(result)
