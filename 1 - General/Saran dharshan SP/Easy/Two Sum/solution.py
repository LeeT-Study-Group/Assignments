class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m ={}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in m:
                return [m[diff],i]
            m[nums[i]] = i
        return []
