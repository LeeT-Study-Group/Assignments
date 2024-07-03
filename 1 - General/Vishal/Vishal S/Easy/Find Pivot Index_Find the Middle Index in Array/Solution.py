class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(1,l):
            nums[i] += nums[i-1]
        
        for i in range(l):
            prev = nums[i-1] if i-1 >=0 else 0
            nxt = (nums[-1]-nums[i]) if i != (l-1) else 0
            if  prev == nxt:
                return i
        return -1