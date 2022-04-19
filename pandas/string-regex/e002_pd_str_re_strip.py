import pandas as pd
color1 = pd.Index([' Green', 'Black ', ' Red ', 'White', ' Pink '])
print("Original series:")
print(color1)

print("\nRemove whitespace")
print(color1.str.strip())
print("\nRemove left sided whitespace")
print(color1.str.lstrip())
print("\nRemove Right sided whitespace")
print(color1.str.rstrip())
