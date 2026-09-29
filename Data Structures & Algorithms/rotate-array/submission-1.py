class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        lst=nums[n-k:n]+nums[0:n-k]
        for i in range(n):
            nums[i]=lst[i]


        