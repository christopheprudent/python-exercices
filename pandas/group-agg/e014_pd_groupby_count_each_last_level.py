import pandas as pd
df = pd.DataFrame( {'id' : [1, 2, 1, 1, 2, 1, 2, 1], 
                    'type' : [10, 15, 11, 20, 21, 12, 14, 10], 
                    'book' : ['Math','English','Physics','Math','English','Physics','English', 'English']})

print("Original DataFrame:")
print(df)

result = df.groupby(['id', 'type', 'book']).size().unstack(fill_value=0)
print("\nResult:")
print(result)
