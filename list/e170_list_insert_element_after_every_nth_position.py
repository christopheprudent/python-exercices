# web solution
def insert_elemnt_nth(lst, ele, n):
    result = []
    for st_idx in range(0, len(lst), n):
        result.extend(lst[st_idx:st_idx+n])
        result.append(ele)
    if len(lst)%n:
        result.pop()
    return result

nums = [1,2,3,4,5,6,7,8,9,10,11]
print('liste', nums)
print('avec élément {}, inséré tous les {} éléments : {}'.format('a', 2, insert_elemnt_nth(nums, 'a', 2)))
