import pandas as pd
import numpy as np
num_series = pd.Series(np.random.randint(1, 10, 20))
print('série')
print(num_series)
result = np.where(num_series % 5==0)
print(type(result))
print("positions & valeurs des multiples de 5")
print(result)
print(num_series.iloc[result])
