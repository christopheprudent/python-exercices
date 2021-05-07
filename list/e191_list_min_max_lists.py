def min_max_lists(*lists):
    _min = min(e for l in lists for e in l)
    _max = max(e for l in lists for e in l)

    return _min, _max
            
print('min/max')
print(min_max_lists(
      [2, 3, 5, 8, 7, 2, 3]
    , [4, 3, 9, 0, 4, 3, 9]
    , [2, 1, 5, 6, 5, 5, 4]
))
