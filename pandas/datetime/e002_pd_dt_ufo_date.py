import pandas as pd
UFO_FILE=r'/home/christophe/Téléchargements/ufo-100.csv'
df = pd.read_csv(UFO_FILE)
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
now = pd.to_datetime('today')
print("Original Dataframe:")
print(df.head())
print("\nCurrent date:")
print(now)
