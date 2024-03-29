import pandas as pd
import numpy as np

df = pd.DataFrame({
    'student_id': ['S001','S001','S002','S002','S003','S003'],
    'marks': [[88,89,90],[78,81,60],[84,83,91],[84,88,91],[90,89,92],[88,59,90]]})
print("Original DataFrame:")
print(df)

print("\nGroupby and aggregate over multiple lists:")
print("* as list")
result = df.set_index('student_id')['marks'].groupby('student_id').apply(list)
print(result)
#result = df.set_index('student_id')['marks'].groupby('student_id').apply(list).apply(lambda x: np.mean(x,0))
#print(result)
print("* eval mean for each group")
result = df.set_index('student_id')['marks'].groupby('student_id').apply(list).apply(lambda x: np.mean(x, axis=0))
print(result)
