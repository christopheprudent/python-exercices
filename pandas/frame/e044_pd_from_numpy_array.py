import pandas
import numpy
dtype = [('Column1','int32'), ('Column2','float32'), ('Column3','float32')]
values = numpy.zeros(15, dtype=dtype)
index = ['Index'+str(i) for i in range(1, len(values)+1)]
df = pandas.DataFrame(values, index=index)
print(df)
