import pandas as pd
from collections import Counter
color_series = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
print("Original Series:")
print(color_series)
print("\nFiltered words:")
# get(i, 0): get vowel (i) if exists, else return default as 0
result = color_series.map(lambda c: sum([Counter(c.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
# result as list of bool values
print(result)
print(color_series[result])
