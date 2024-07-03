class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        for idx, num in enumerate(nums):
            if target - num in storage:
                return idx, storage[target-num]
            storage[num] = idx