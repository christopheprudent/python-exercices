# web solution
import itertools as it

def test(lst):
    # groupby retourne n tuples (clé, groupe)
    result = [ list(x[1]) for x in it.groupby(lst, lambda x: x == 0) if not x[0] ]
    return result

if __name__ == '__main__':
    nums = [3,4,6,2,0,0,0,0,0,0,6,7,6,9,10,0,0,0,0,0,7,4,4,0,0,0,0,0,0,5,3,2,9,7,1]
    print('liste', nums)
    '''
    [ (k, list(g)) for k,g in itertools.groupby(nums, lambda x: x==0) ]
    [(False, [3, 4, 6, 2]), (True, [0, 0, 0, 0, 0, 0]), (False, [6, 7, 6, 9, 10]), (True, [0, 0, 0, 0, 0]), (False, [7, 4, 4]), (True, [0, 0, 0, 0, 0, 0]), (False, [5, 3, 2, 9, 7, 1])]
    '''
    print('blocks de données non nulles', test(nums))
