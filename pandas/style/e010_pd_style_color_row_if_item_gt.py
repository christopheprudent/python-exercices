import pandas as pd
import numpy as np

np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
               axis=1)
print("Original array:")
print(df)
print("number of columns", len(df.columns))
print("\nDataframe - table style:")

def highlight_greaterthan(x):
    _cols = len(x.columns)
    if x.C > .5:
        return ['background-color: yellow']*_cols
    else:
        return ['background-color: white']*_cols 

result = df.style.apply(highlight_greaterthan, axis=1)
print(result)
