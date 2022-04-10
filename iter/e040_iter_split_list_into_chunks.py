# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
from itertools import islice

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

# web solution
def split_list(lst, n):
    lst = iter(lst)
    result = iter(lambda: tuple(islice(lst, n)), ())
    return list(result)

if __name__ == '__main__':
    nums = [12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]

    print('liste', nums)
    for n in range(3, 7):
        print('liste subdivisée en morceaux de taille %d' % (n))
        print('web1', list(chunk(nums, n)))
        print('web2', split_list(nums, n))
