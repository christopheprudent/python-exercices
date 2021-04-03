#a = list([1, 2, 3, 4, 5, 6, 7, 8, 9])
#while len(a) >= 3:
#	print('3e élément=', a[2])
#	del a[2]

def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1 
  idx = 0
  len_list = len(int_list)
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1

nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)

