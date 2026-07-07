class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst=set()
        for num in nums:
            if num in lst:
                return True
            else:
                lst.add(num)
        return False
        