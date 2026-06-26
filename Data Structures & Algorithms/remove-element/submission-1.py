class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ls=[]
        for num in nums:
            if val!=num:
                ls.append(num)
        nums[:]=ls
        return len(ls)
