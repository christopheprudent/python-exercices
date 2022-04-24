import pandas as pd
time_series = pd.date_range('1/1/2021', periods = 16, freq='3M')

'''
dates trimestrielles (mais fin de mois ?)
DatetimeIndex(['2021-01-31', '2021-04-30', '2021-07-31', '2021-10-31',
               '2022-01-31', '2022-04-30', '2022-07-31', '2022-10-31',
               '2023-01-31', '2023-04-30', '2023-07-31', '2023-10-31',
               '2024-01-31', '2024-04-30', '2024-07-31', '2024-10-31'],
              dtype='datetime64[ns]', freq='3M')
'''
print("Time series using three months frequency:")
print(time_series) 
