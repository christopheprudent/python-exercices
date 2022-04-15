import pandas as pd
import numpy as np
df = pd.DataFrame([1000, 2000, 3000, -4000, np.inf, -np.inf])
print("Original DataFrame:")
print(df)
print("Removing infinite values:")
df = df.replace([np.inf, -np.inf], np.nan)
print(df)
