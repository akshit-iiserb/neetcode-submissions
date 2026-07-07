class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=[]
        for i in s:
            if i not in {",","'","?"," ",".",":",";"}:
                lst.append(i.lower())
        return lst==lst[::-1]
        

        