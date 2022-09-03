import pandas as pd

FILE_EXCEL='/home/christophe/Téléchargements/SaleData.xlsx'

df = pd.read_excel(FILE_EXCEL)
print(df)

# eval mean (default agg) on numeric columns, grouped by 'index' values
#
#                       Sale_amt   Unit_price      Units
#Region  SalesMan                                       
#Central David      28191.000000   724.200000  42.600000
#        John       41338.666667   607.666667  52.000000
#        Luis       41274.600000   690.900000  56.200000
#        Shelli      8424.500000   185.500000  48.250000
#        Sigal      41679.166667   585.500000  57.666667
#        Steven     49922.500000  1023.500000  45.750000
#East    Alexander  29587.875000   529.750000  49.500000
#        Diana      18050.000000   362.500000  62.500000
#        Karen      16068.000000   261.166667  56.666667
#West    Michael    33418.000000   849.000000  44.500000
#        Stephen    22015.750000   512.000000  35.500000

result = pd.pivot_table(df,index=["Region","SalesMan"])
print(result)
