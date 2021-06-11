# web solution
from bisect import bisect, bisect_left
from collections import Counter

class Solution:
    def three_Sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        if len(nums) < 3:
            return triplets
        num_freq = Counter(nums)
        nums = sorted(num_freq)  # Sorted unique numbers
        max_num = nums[-1]
        print(f' nums={nums} max_num={max_num}')
        for i, v in enumerate(nums):
            print(f' i={i} v={v}')
            if num_freq[v] >= 2:
                complement =  -2 * v
                if complement in num_freq:
                    print(f' complement={complement}')
                    if complement != v or num_freq[v] >= 3:
                        triplets.append([v] * 2 + [complement])
                        print(f' cas 1 : triplets={triplets}')

            # When all 3 numbers are different.
            if v < 0:  # Only when v is the smallest
                two_sum = -v

                # Lower/upper bound of the smaller of remaining two.

                # left
                #  left-part:  all(val <  x for val in a[lo:i])
                #  right-part: all(val >= x for val in a[i:hi])
                lb = bisect_left(nums, two_sum - max_num, i + 1)
                # right
                #  left-part:  all(val <= x for val in a[lo:i])
                #  right-part: all(val >  x for val in a[i:hi])
                ub = bisect(nums, two_sum // 2, lb)                       

                print(f' two_sum={two_sum}')
                print(f' search lo={two_sum - max_num} from {i+1}')
                print(f' search hi={two_sum // 2} from {lb}')
                print(f' lb={lb} ub={ub} : {nums[lb : ub]}')
                print(f' lb : left {nums[i+1:lb]} right {nums[lb:]}')
                print(f' ub : left {nums[lb:ub]} right {nums[ub:]}')
                for u in nums[lb : ub]:
                    print(f' u={u}')
                    complement = two_sum - u
                    if complement in num_freq and u != complement:
                        print(f' complement={complement}')
                        triplets.append([v, u, complement])
                        print(f' cas 2 : triplets={triplets}')
        return triplets

nums = [-20, 0, 20, 40, -20, -40, 80]
print('liste', nums)
s = Solution()
result = s.three_Sum(nums)
print('solution:', result)

print()
print('liste', nums)
nums = [1, 2, 3, 4, 5, -6]
result = s.three_Sum(nums)
print('solution:', result)
