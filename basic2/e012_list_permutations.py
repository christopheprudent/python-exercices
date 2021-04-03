def permute(nums):
  result_perms = [[]]
  for n in nums:
    print('n=%d' % n)
    new_perms = []
    for perm in result_perms:
      print('perm=%s len=%d' %(str(perm), len(perm)))
      for i in range(len(perm)+1):
        print('i=%d' % i)
        new_perms.append(perm[:i] + [n] + perm[i:])
        print('new_perms=%s' % str(new_perms))
        result_perms = new_perms
  return result_perms

my_nums = [1,2,3]
print("Original Cofllection: ",my_nums)
print("\nCollection of distinct numbers:\n",permute(my_nums))

# import itertools
# print(list(itertools.permutations(my_nums)))
