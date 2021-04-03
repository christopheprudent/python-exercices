import itertools

def sum_abs_difference_of_distinct_2pairs(arr):
	_pairs=itertools.combinations(arr, 2)
	return sum([abs(x[0] - x[1]) for x in _pairs])

print(sum_abs_difference_of_distinct_2pairs([1,2,3]))
print(sum_abs_difference_of_distinct_2pairs([1,4,5]))
