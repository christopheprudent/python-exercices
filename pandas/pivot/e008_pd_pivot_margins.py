import pandas as pd
import numpy as np

FILE_EXCEL='/home/christophe/Téléchargements/SaleData.xlsx'

df = pd.read_excel(FILE_EXCEL)
print(df)

# eval sum on ['Units', 'Sale_amt'] columns, grouped by ['Manager', 'SalesMan'] values, with a total row
#
#                    Sale_amt   Units
#Manager SalesMan                    
#Douglas John        124016.0   156.0
#        Karen        48204.0   170.0
#        Michael      66836.0    89.0
#Hermann Luis        206373.0   281.0
#        Shelli       33698.0   193.0
#        Sigal       125037.5   173.0
#Martha  Alexander   236703.0   396.0
#        Diana        36100.0   125.0
#        Steven      199690.0   183.0
#Timothy David       140955.0   213.0
#        Stephen      88063.0   142.0
#All                1305675.5  2121.0

# only sale amounts
result = pd.pivot_table(df, index=["Manager", "SalesMan"], values=["Units", "Sale_amt"], aggfunc=np.sum, margins=True)
print(result)
