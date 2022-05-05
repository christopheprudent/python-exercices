import pandas as pd

# https://pandas.pydata.org/pandas-docs/version/0.13.1/timeseries.html
# annual frequency, anchored end of December. Same as ‘A’

ytp = pd.Period('2022', 'A-DEC')
print("Yearly time period:", ytp)
print("\nAll the properties of the said period:")
print(dir(ytp))
