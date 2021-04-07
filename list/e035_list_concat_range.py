def concat_range(l, n):
	t = []
	for i in range(1, n+1):
		for x in l:
			#print(f'x={x} i={i}')
			#print(type(x))
			t.append(x+str(i))

	return t

print(concat_range(['p', 'q'], 5))

# web solution
my_list = ['p', 'q']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)

