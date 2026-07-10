class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lst=[]
        count=0
        for i in range(len(nums)):
            if nums[i]==0:
                lst.append(count)
                count=0
            elif i==len(nums)-1 and nums[i]==1:
                count+=1
                lst.append(count)
            else:
                count+=1
        return max(lst)
