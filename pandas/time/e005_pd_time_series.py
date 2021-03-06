import pandas as pd
import numpy as np
from datetime import datetime, date

dates = [datetime(2011, 9, 1), datetime(2011, 9, 2)]
print("Time-series with two index labels:")
time_series = pd.Series(np.random.randn(2), dates)
print(time_series)
print("\nType of the index:")
print(type(time_series.index))
