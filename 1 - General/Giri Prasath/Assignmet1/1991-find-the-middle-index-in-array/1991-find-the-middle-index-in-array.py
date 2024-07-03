class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ssum = sum(nums)
        countl = 0
        
        for i in range(len(nums)):
            countr = ssum-nums[i]-countl
            if countl == countr:
                return i
            countl += nums[i]
        
        return -1