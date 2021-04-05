list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]

diff = (set(list1) - set(list2)) | (set(list2) -set(list1))
print('Différence entre listes {} et {} vaut : {}'.format(list1, list2, list(diff)))
