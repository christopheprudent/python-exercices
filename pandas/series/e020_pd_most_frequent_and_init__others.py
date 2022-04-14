import pandas as pd
import numpy as np
np.random.RandomState(100)
num_series = pd.Series(np.random.randint(1, 5, 15))
print('série')
print(num_series)
print('fréquence')
print(num_series.value_counts())
num_series[~num_series.isin(num_series.value_counts().index[:1])] = 'Other'
print('init valeurs autres que la plus fréquente')
print(num_series)
