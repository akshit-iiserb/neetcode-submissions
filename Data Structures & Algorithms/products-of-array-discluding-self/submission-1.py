class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ls=[1]*n
        rs=[1]*n
        for i in range(1,n):
            ls[i]=ls[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            rs[i]=rs[i+1]*nums[i+1]
        output=[1]*n
        for i in range(n):
            output[i]=ls[i]*rs[i]
        return output
        