class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        p=""

        for char in s:
            if ord(char)>=97 and ord(char)<=122 or ord(char)>=48 and ord(char)<=57:
                p+=char
        
        rev=""

        for i in range(len(p)-1,-1,-1):
            rev+=p[i]
        
        return rev==p