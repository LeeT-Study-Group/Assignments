class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        sums = 0
        
        for i, num in enumerate(nums):
            if sums == (total_sum - sums - num):
                return i
            sums += num
        
        return -1