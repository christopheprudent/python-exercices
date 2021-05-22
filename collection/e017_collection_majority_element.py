# web solution
import collections
#class Solution(object):
class Solution():
    def majorityElement(self, nums):
        """
        Note:   The majority element algorithm finds a majority element, if there is one: 
                that is, an element that occurs repeatedly for more than half of the elements of the input.
        :type nums: List[int]
        :return type: int
        """
        count_ele=collections.Counter(nums)
        most = count_ele.most_common()[0][0]
        majority = None
        if count_ele[most] / sum(count_ele.values()) >= .5:
            majority = most
        return majority

#result = Solution().majorityElement([10,10,20,30,40,10,20,10])
sol = Solution()
result = sol.majorityElement([10,10,20,30,40,10,20,10,20])

print(result)
