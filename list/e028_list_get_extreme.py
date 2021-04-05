# derived from web soution
def get_extreme(numbers, _from='begin', item= 1):
  if (len(numbers)<item):
    return
  if ((len(numbers)==item)  and (all(numbers[i] == numbers[i+1] for i in range(item -2)) )):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()
  if _from == 'begin':
    _item = item -1
  else:
    _item = item * (-1)
  return uniq_items[_item]   

# 2nd smallest
print(get_extreme([1,2,3,4,4], _from='begin', item= 2))
print(get_extreme([1, 1, 1, 0, 0, 0, 2, -2, -2], _from='begin', item= 2))
print(get_extreme([2,2], _from='begin', item= 2))
print(get_extreme([1], _from='begin', item= 2))

# 2nd largest
print(get_extreme([1,2,3,4,4], _from='end', item= 2))
print(get_extreme([1, 1, 1, 0, 0, 0, 2, -2, -2], _from='end', item= 2))
print(get_extreme([2,2], _from='end', item= 2))
print(get_extreme([1], _from='end', item= 2))

