import itertools

def concat_element_wise_lists(*lists):
    return [''.join(list(itertools.chain(*i))) for i in zip(*lists)]

L1 = ['0', '1', '2', '3', '4']
L2 = ['red', 'green', 'black', 'blue', 'white']
L3 = ['100', '200', '300', '400', '500']

print(concat_element_wise_lists(L1, L2, L3))

# web solution
def concatenate_lists(l1,l2,l3):
    return [i + j + k for i, j, k in zip(l1, l2, l3)]

print(concatenate_lists(L1,L2,L3))
