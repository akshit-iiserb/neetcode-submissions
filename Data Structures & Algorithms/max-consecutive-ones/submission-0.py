class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ls=[]
        count=0
        for num in nums:
            if num==1:
                count+=1
            elif num==0:
                ls.append(count)
                count=0
        ls.append(count)
        return max(ls)
        