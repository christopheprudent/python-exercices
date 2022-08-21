import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILE_EXCEL='/home/christophe/Téléchargements/coalpublic2013.xls'

df = pd.read_excel(FILE_EXCEL)
sorted_by_production = df.sort_values(['Production (short tons)'], ascending=False).head(10)
sorted_by_production['Production (short tons)'].plot(kind="barh")
plt.show()
