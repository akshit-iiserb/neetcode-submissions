class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi=len(nums)-1
        lo=0

        while (hi-lo)>1:
            mid=(hi+lo)//2
            if(nums[mid]>target):
                hi=mid
            else:
                lo=mid
        if nums[hi]==target:
            return hi
        elif nums[lo]==target:
            return lo
        else:
            return -1
        



    
        


        