# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.php
# web solution
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
L = [1,2,3,5,8]
print('liste', L)
item = 1
print(f'cherche élément: {item}')
print(binary_search(L, item))
item = 6
print(f'cherche élément: {item}')
print(binary_search(L, item))
item = 5
print(f'cherche élément: {item}')
print(binary_search(L, item))
item = 8
print(f'cherche élément: {item}')
print(binary_search(L, item))
