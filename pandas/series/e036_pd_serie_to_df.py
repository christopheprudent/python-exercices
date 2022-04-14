import numpy as np
import pandas as pd
char_list = list('ABCDEFGHIJKLMNOP')
num_range = np.arange(8)
num_dict = dict(zip(char_list, num_range))
print(f'list={char_list} nr={num_range} nd={num_dict}')
s = pd.Series(num_dict)
print(s)
df = s.to_frame().reset_index()
print(df)
