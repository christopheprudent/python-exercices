import pandas as pd
s = pd.Series(['php', 'python', 'java', 'c#', '', 'hello'])
print('serie')
print(s)
result = s.map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper() if len(x) > 0 else x)
print("\nFirst and last character of each word to upper case:")
print(result)
