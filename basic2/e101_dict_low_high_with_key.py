def oldest_student(students):
	return max(students, key=students.get)

d = {"Bernita Ahner": 12, "Kristie Marsico": 11, "Sara Pardee": 14, "Fallon Fabiano": 11, "Nidia Dominique": 15}
# dict(sorted(d.items(), key= lambda x: x[1]))
sl = sorted(d.items(), key= lambda x: x[1])
print('youngest student is :', sl[0][0], 'age=', sl[0][1])
print('oldest student is :', sl[-1][0], 'age=', sl[-1][1])
print('oldest student is :', oldest_student(d))

# https://stackoverflow.com/questions/3108042/get-max-key-in-dictionary
MyCount= {u'10': 1, u'1': 2, u'3': 2, u'2': 2, u'5': 3, u'4': 2, u'7': 2, u'6': 2, u'9': 2, u'8': 2}
print(MyCount)
print('get("10")={}'.format(MyCount.get('10')))
print('get("4")={}'.format(MyCount.get('4')))
print(max(MyCount, key=int))
# https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
# find key with Maximum value in Dictionary
print(max(MyCount, key=MyCount.get))
