def is_list_increasing_trend(l):
	# web solution
	#return (sorted(l) == l)
	return all(x < y for x,y in zip(l, l[1:]))

print(is_list_increasing_trend([1,2,3,4]))
print(is_list_increasing_trend([1,2,5,3,4]))
print(is_list_increasing_trend([-1,-2,-3,-4]))
print(is_list_increasing_trend([-4,-3,-2,-1]))
print(is_list_increasing_trend([1,2,3,4,0]))

