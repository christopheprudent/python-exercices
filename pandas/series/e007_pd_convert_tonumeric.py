import pandas as pd
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print('serie')
print(s1)
print("Change the said data type to numeric:")

# errors{‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’
#If ‘raise’, then invalid parsing will raise an exception.
#If ‘coerce’, then invalid parsing will be set as NaN.
#If ‘ignore’, then invalid parsing will return the input.

s2 = pd.to_numeric(s1, errors='coerce')
print(s2)
