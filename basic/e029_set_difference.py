def in_set(set, item):
	if item in set:
		return True

	return False

color_set_1 = {'white', 'black', 'red'}
color_set_2 = {'green', 'red'}

color_not_in_set = set()
for color in color_set_1:
	if not in_set(color_set_2, color):
		color_not_in_set.add(color)

print(color_not_in_set)
