#def cumulative_sum(a):
#	if len(a) == 0:
#		return 0
#
#	_sum=[]
#	for i, v in enumerate(a):
#		if i == 0:
#			_sum.append(v)
#		else:
#			_sum.append(_sum[i-1] + v)
#
#	return _sum

#print(cumulative_sum([10, 20, 30, 40, 50, 60, 7]))
#print(cumulative_sum([1, 2, 3, 4, 5]))
#print(cumulative_sum([0, 1, 2, 3, 4, 5]))

# web solution
def nums_cumulative_sum(nums_list):
  return [sum(nums_list[:i+1]) for i in range(len(nums_list))]

print(nums_cumulative_sum([10, 20, 30, 40, 50, 60, 7]))
print(nums_cumulative_sum([1, 2, 3, 4, 5]))
print(nums_cumulative_sum([0, 1, 2, 3, 4, 5]))

