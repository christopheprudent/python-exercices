def remove_all_instances(a, i):
	while True:
		try:
			a.remove(i)
		except ValueError:
			break

	return a

print(remove_all_instances([1, 2, 3, 4, 5, 6, 7, 5], 5))
print(remove_all_instances([10,10,10,10,10], 10))
print(remove_all_instances([10,10,10,10,10], 20))
print(remove_all_instances([], 1))
