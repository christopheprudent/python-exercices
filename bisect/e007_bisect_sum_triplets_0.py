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
        print(f'nums={nums} max_num={max_num}')
        for i, v in enumerate(nums):
            print(f'i={i} v={v}')
            if num_freq[v] >= 2:
                complement =  -2 * v
                if complement in num_freq:
                    print(f'complement={complement}')
                    if complement != v or num_freq[v] >= 3:
                        triplets.append([v] * 2 + [complement])
                        print(f'triplets={triplets}')

            # When all 3 numbers are different.
            if v < 0:  # Only when v is the smallest
                two_sum = -v
                print(f'two_sum={two_sum}')
                print(f'search lo={two_sum - max_num}')
                print(f'search hi={two_sum // 2}')

                # Lower/upper bound of the smaller of remaining two.
                lb = bisect_left(nums, two_sum - max_num, i + 1)
                ub = bisect(nums, two_sum // 2, lb)                       
                print(f'lb={lb}')
                print(f'ub={ub}')
                for u in nums[lb : ub]:
                    complement = two_sum - u
                    print(f'complement={complement} u={u}')
                    if complement in num_freq and u != complement:
                        triplets.append([v, u, complement])
                        print(f'triplets={triplets}')
        return triplets

nums = [-20, 0, 20, 40, -20, -40, 80]
print('liste', nums)
s = Solution()
result = s.three_Sum(nums)
print(result)

print()
print('liste', nums)
nums = [1, 2, 3, 4, 5, -6]
result = s.three_Sum(nums)
print(result)
