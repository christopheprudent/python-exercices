import pandas as pd

# BQS-JUN: quarterly frequency, year ends in June
#q_start_dates = pd.date_range('2020-01-01', '2020-12-31', freq='BQS-JUN')
q_start_dates = pd.date_range('2020-01-01', '2020-12-31', freq='QS')
#q_end_dates = pd.date_range('2020-01-01', '2020-12-31', freq='BQ-JUN')
q_end_dates = pd.date_range('2020-01-01', '2020-12-31', freq='Q')
print("All the quarterly begin dates of 2020:")
print(q_start_dates.values)
print("\nAll the quarterly end dates of 2020:")
print(q_end_dates.values)

print("\nBusiness")
bq_start_dates = pd.bdate_range('2020-01-01', '2020-12-31', freq='BQS')
bq_end_dates = pd.bdate_range('2020-01-01', '2020-12-31', freq='BQ')
print(bq_start_dates.values)
print(bq_end_dates.values)
