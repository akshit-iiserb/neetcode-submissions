class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s):
            return s==s[::-1]
        i=0
        j=len(s)-1
        while(i<j):
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
               return check(s[i+1:j+1]) or check(s[i:j])
        return True
        