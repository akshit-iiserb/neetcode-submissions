# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        hi=n
        lo=0
        result=0
        while (hi>=lo):
            mid=(hi+lo)//2
            result=guess(mid)
            if result==0:
                return mid
            elif result==-1:
                hi=mid
            else:
                lo=mid+1
        

        