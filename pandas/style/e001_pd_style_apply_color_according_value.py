import pandas as pd
import numpy as np

np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
               axis=1)
print("Original array:")
print(df)

def color_negative_red_else_black(val):
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color

print("\nNegative numbers red and positive numbers black:")
result = df.style.applymap(color_negative_red_else_black)
# https://stackoverflow.com/questions/58116600/pandas-styler-not-printing-dataframe-to-spyders-console-as-expected/58118375#58118375
# no output now!
print(result)
