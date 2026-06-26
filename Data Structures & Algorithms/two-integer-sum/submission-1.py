class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        duplicate=nums[:]
        for i in range(len(nums)):
            val = nums[i]
            req=target - val
            duplicate[i] = None
            if req in duplicate:
                return [i, duplicate.index(req)]
        return []