import bisect

# web solution
my_list = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
print('{:<15} : {}'.format('liste', my_list))

sorted_list = []
for i in my_list:
    #position = bisect.bisect(sorted_list, i)
    bisect.insort(sorted_list, i)

print('{:<15} : {}'.format('liste triée', sorted_list))
