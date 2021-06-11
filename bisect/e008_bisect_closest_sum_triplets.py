# web solution
#Source: https://bit.ly/2SRefdb
from bisect import bisect, bisect_left
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        print('nums', nums)
        # Let top[i] be the sum of largest i numbers.
        top = [
            0,
            nums[-1],
            nums[-1] + nums[-2]
        ]
        print('top', top)
        min_diff = float('inf')
        three_sum = 0

        # Find range of the least number in curr_n (0, 1, 2 or 3)
        # numbers that sum up to curr_target, then find range of 
        # 2nd least number and so on by recursion. 
        def closest(curr_target, curr_n, lo=0, deep=1):
            print('{} curr_target={} curr_n={} lo={}'.format(' ' * deep, curr_target, curr_n, lo))
            if curr_n == 0:
                nonlocal min_diff, three_sum
                if abs(curr_target) < min_diff:
                    min_diff = abs(curr_target)
                    three_sum = target - curr_target
                    print('{} min_diff={} three_sum={}'.format(' ' * deep, min_diff, three_sum))
                return

            next_n = curr_n - 1
            print('{} next_n={}'.format(' ' * deep, next_n))
            max_i = len(nums) - curr_n
            print('{} max_i={}'.format(' ' * deep, max_i))
            max_i = bisect(
                nums, curr_target // curr_n,
                lo, max_i)
            print('{} max_i={}'.format(' ' * deep, max_i))
            min_i = bisect_left(
                nums, curr_target - top[next_n],
                lo, max_i) - 1
            print('{} min_i={}'.format(' ' * deep, min_i))
            min_i = max(min_i, lo)
            print('{} min_i={}'.format(' ' * deep, min_i))

            for i in range(min_i, max_i + 1): 
                print('{} i={} min_diff={}'.format(' ' * deep, i, min_diff))
                if min_diff == 0:
                    return
                if i == min_i or nums[i] != nums[i - 1]:
                    next_target = curr_target - nums[i]
                    print('{} next_target={}'.format(' ' * deep, next_target))
                    closest(next_target, next_n, i + 1, deep +1)

        closest(target, 3)
        return three_sum

s = Solution()
nums = [1, 2, 3, 4, 5, -6]
target = 14
print("\ntableau & valeur cible:", nums, "&", target)
result = s.threeSumClosest(nums, target)
print("Somme triplets la plus proche de la cible:", result)

#nums = [1, 2, 3, 4, -5, -6]
#target = 5
#print("\ntableau & valeur cible:", nums, "&", target)
#result = s.threeSumClosest(nums, target)
#print("Somme triplets la plus proche de la cible:", result)
