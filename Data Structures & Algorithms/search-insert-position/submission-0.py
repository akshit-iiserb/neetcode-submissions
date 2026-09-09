class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if (target>nums[-1]):
            return len(nums)
        if (target<nums[0]):
            return 0
        hi=len(nums)-1
        lo=0
        while (hi-lo)>1:
            mid=(hi+lo)//2
            if (nums[mid]>=target):
                hi=mid
            else:
                lo=mid
        if(nums[hi]==target):
            return hi
        elif(nums[lo]==target):
            return lo
        elif(nums[lo]<target):
            return lo+1
        
        


        