def recursion_sum_of_list(l, i=0):
    if i == len(l):
        return 0
    else:
        sum_i = sum(l[i]) if isinstance(l[i], list) else l[i]
        return sum_i + recursion_sum_of_list(l, i+1)

# web solution (mix)
def list_sum(num_List):
    sum_0 = sum(num_List[0]) if isinstance(num_List[0], list) else num_List[0]
    if len(num_List) == 1:
        return sum_0
    else:
        return sum_0 + list_sum(num_List[1:])

# web solution
def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total

if __name__ == '__main__':
    tests = [1, [5, 1], -2, 60, [2, 15]]
    print('dev) somme des valeurs de', tests, 'égale à', recursion_sum_of_list(tests))
    print('mix) somme des valeurs de', tests, 'égale à', list_sum(tests))
    print('web) somme des valeurs de', tests, 'égale à', recursive_list_sum(tests))
