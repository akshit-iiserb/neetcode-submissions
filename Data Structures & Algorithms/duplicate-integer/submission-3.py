class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=[]
        for num in nums:
            if num in count:
                return True
            else:
                count.append(num)
        return False