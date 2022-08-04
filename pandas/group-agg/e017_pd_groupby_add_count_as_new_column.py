import pandas as pd
df = pd.DataFrame({
'book_name':['Book1','Book2','Book3','Book4','Book1','Book2','Book3','Book5'],
'book_type':['Math','Physics','Computer','Science','Math','Physics','Computer','English'],
'book_id':[1,2,3,4,1,2,3,5]})
print("Original Orders DataFrame:")
print(df)
# When we reset the index, the old index is added as a column, and a new sequential index is used
print("\nNew column with count from groupby:")
result = df.groupby(["book_name", "book_type"])["book_type"].count().reset_index(name="count")
print(result)
