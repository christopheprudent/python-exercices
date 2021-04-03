def get_median_list(data):
	c = len(data)
	if c == 0:
		return None
	if c == 1:
		return data[0]

	p = c // 2
	if not c % 2:
		return (data[p-1] + data[p]) / 2
	else:
		return data[p]

print(get_median_list([1,2,3,4,5]))
print(get_median_list([1,2,3,4,5,6]))
print(get_median_list([6,1,2,4,5,3]))
print(get_median_list([1.0,2.11,3.3,4.2,5.22,6.55]))
print(get_median_list([1.0,2.11,3.3,4.2,5.22]))
print(get_median_list([2.0,12.11,22.3,24.12,55.22]))
		
