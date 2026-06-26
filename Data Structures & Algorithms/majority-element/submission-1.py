class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         d={}
         for i in nums:
            d[i]=d.get(i,0)+1
         for i in set(nums):
            if d[i]>(len(nums)/2):
                return i