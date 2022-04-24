import pandas as pd
import numpy as np
from datetime import datetime, date 

dates = ['2014-08-01','2014-08-02','2014-08-03','2014-08-04']
time_series = pd.Series(np.random.randn(len(dates)), dates)
print(time_series)
