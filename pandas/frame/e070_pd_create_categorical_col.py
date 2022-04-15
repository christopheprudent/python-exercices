import pandas as pd
df = pd.DataFrame({
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton', 'Kierra Gentry'],
      'age': [18, 22, 85, 50, 80, 5]
})
print("Original DataFrame:")
print(df)
print('\nAge group:')
df["age_groups"] = pd.cut(df["age"], bins = [0, 18, 65, 99], labels = ["kids", "adult", "elderly"])
print(df["age_groups"])
