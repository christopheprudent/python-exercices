import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILE_EXCEL='/home/christophe/Téléchargements/coalpublic2013.xlsx'

df = pd.read_excel(FILE_EXCEL)
df[['Production', 'Labor_Hours']].head(10).plot(kind='bar', figsize=(20,8))
plt.show()
