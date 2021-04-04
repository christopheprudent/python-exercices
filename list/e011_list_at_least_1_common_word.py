def common_word(l1, l2):
	return any(w in l2 for w in l1)

list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
print(common_word(list1, list2))

del list2[0]
print(common_word(list1, list2))
