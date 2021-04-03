def digit_distance(x,y):
	sx = str(x)
	sy = str(y)
	if len(sx) != len(sy):
		return None

	return sum(abs(int(sx[i]) - int(sy[i])) for i in range(len(sx)))

# web solution
# eval absolute difference between x and y, transform to string, and sum each digit!
def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))

print(digit_distance(123, 256))
print(digit_distance(23, 56))
print(digit_distance(1, 2))
print(digit_distance(24232, 45645))
