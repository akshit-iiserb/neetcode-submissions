class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct={}
        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]]=1
            else:
                dct[nums[i]]+=1
        for num in dct:
            if dct[num]>1:
                return True
        return False