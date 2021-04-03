def three_sum(nums):
  result = []
  nums.sort()
  print(nums)
  for i in range(len(nums)-2):
    print('i=%i' %i)
    if i> 0 and nums[i] == nums[i-1]:
      continue
    l, r = i+1, len(nums)-1
    while l < r:
      s = nums[i] + nums[l] + nums[r]
      print('l=%i, r=%i, s=%i' %(l,r,s))
      if s > 0:
        r -= 1
      elif s < 0:
          l += 1
      else:
        # found three sum
        print('(i,l,r)=',(i,l,r),)
        result.append((nums[i], nums[l], nums[r]))
        return result
        # remove duplicates? useful ???
        while l < r and nums[l] == nums[l+1]:
          l+=1
          while l < r and nums[r] == nums[r-1]:
            r -= 1
            l += 1
            r -= 1
          print('(i,l,r)=(%i,%i,%i)' %(i,l,r))
          return result

x = [1, -6, 4, 2, -1, 2, 0, -2, 0, 4 ]
print(three_sum(x))

