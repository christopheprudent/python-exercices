import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 2))
print("Original DataFrame:")
print(df)
part_70 = df.sample(frac=0.7,random_state=10)
part_30 = df.drop(part_70.index)
print("\n70% of the said DataFrame:")
print(part_70)
print("\n30% of the said DataFrame:")
print(part_30)
