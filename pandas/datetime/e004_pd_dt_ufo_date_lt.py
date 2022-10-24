import pandas as pd
import datetime

UFO_FILE=r'/home/christophe/Téléchargements/ufo.csv'
df = pd.read_csv(UFO_FILE)
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')

print("Original Dataframe:")
print(df.head())

now = pd.to_datetime('today')
duration = datetime.timedelta(days=365*40)

print("\nSighting days of the unidentified flying object (ufo) which are less than or equal to 40 years (365*40 days):")
print(df[now - df['Date_time'] <= duration])
