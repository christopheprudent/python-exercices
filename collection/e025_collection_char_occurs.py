import collections

def get_occurs_less_more_than(l, n):
    d = collections.defaultdict(int)
    for s in l:
        for c in s:
            d[c] += 1

    less = [k for k, v in d.items() if v < n]
    more = [k for k, v in d.items() if v > n]
    return less, more

# web solution
from itertools import chain 
def max_aggregate(list_str, N):
    temp = (set(sub) for sub in list_str) 
    counts = collections.Counter(chain.from_iterable(temp)) 
    print(counts)

    temp = (set(sub) for sub in list_str) 
    #[{'a', 'd', 'c', 'b'}, {'i', 'b', 'a', 'h', 'e', 'f'}, {'a', 'l', 's', 'd', 'f'}, {'a', 'd', 'f', 's'}, {'l', 'j', 'k', 'd', 'g', 'f'}]
    print(list(temp))

    gt_N =  [chr for chr, count in counts.items() if count > N]
    lt_N =  [chr for chr, count in counts.items() if count < N]
    return gt_N, lt_N

L = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
print('liste', L)
noccurs = 3
lt, gt = get_occurs_less_more_than(L, noccurs)
print('liste des lettres {} trouvées moins de {} fois'.format(lt, noccurs))
print('liste des lettres {} trouvées plus de {} fois'.format(gt, noccurs))

lt, gt = max_aggregate(L, noccurs)
print('liste des lettres {} trouvées moins de {} fois'.format(lt, noccurs))
print('liste des lettres {} trouvées plus de {} fois'.format(gt, noccurs))
