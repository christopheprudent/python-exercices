import itertools

def avg_list_by_position(ll):
    # FIXME
    # moyenne calculée avec extension à 0 pour les listes plus petites, ce qui fausse le résultat!
    #return [sum(x)/float(len(x)) for x in itertools.zip_longest(*ll, fillvalue=0)]

    return [sum([n for n in x if n != None])/float(len([n for n in x if n != None])) for x in itertools.zip_longest(*ll)]

# web solution
import itertools as it
def avg_lists_diff_length(nums):
    def get_avg(x):
        x = [i for i in x if i is not None]
        return sum(x, 0.0) / len(x)
    result = map(get_avg, it.zip_longest(*nums))
    return list(result)

L = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
print('liste', L)
print('moyennes par position respective')
print(avg_list_by_position(L))
print(avg_lists_diff_length(L))
