import array

def all_uniq_values(a):
    return all(a.count(x) == 1 for x in a)

# web solution
def test_duplicate(array_nums):
    nums_set = set(array_nums)    
    return len(array_nums) != len(nums_set)     

L = [1,2,3,4,5]
print('liste', L)
print('valeurs dupliquées', test_duplicate(L))
print('valeurs uniques', all_uniq_values(L))
L = [1,2,3,4,4]
print('liste', L)
print('valeurs dupliquées', test_duplicate(L))
print('valeurs uniques', all_uniq_values(L))
L = [1,1,2,2,3,3,4,4,5]
print('liste', L)
print('valeurs dupliquées', test_duplicate(L))
print('valeurs uniques', all_uniq_values(L))
