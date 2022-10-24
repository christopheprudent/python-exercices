import pandas as pd
UFO_FILE=r'/home/christophe/Téléchargements/ufo-100.csv'
df = pd.read_csv(UFO_FILE)
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')

print("Original Dataframe:")
print(df.head())

print("\nCurrent date of Ufo dataset:")
print(df.Date_time.max())
print("\nOldest date of Ufo dataset:")
print(df.Date_time.min())
print("\nNumber of days between Current date and oldest date of Ufo dataset:")
print((df.Date_time.max() - df.Date_time.min()).days)
