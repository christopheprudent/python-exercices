import random
import itertools

# web solution
def randomly_interleave(nums1, nums2):
    result =  list(map(next, random.sample([iter(nums1)]*len(nums1) + [iter(nums2)]*len(nums2), len(nums1)+len(nums2))))
    return result

def interleave_two_given_list_into_another_list_randomly(l1, l2):
    _len = len(l1) + len(l2)
    _another = [None] * _len
    for _val in itertools.chain(l1, l2):
        while True:
            _i = random.randint(0, _len-1)
            if _another[_i] is None:
                break

        _another[_i] = _val

    return _another

L1 = [1,2,7,8,3,7]
L2 = [4,3,8,9,4,3,8,9]
print('liste 1', L1)
print('liste 2', L2)
print('après mélange aléatoire')
print('mine:', interleave_two_given_list_into_another_list_randomly(L1, L2))
print(' web:', randomly_interleave(L1, L2))
