class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        string=""
        for char in s:
            if ord(char)>=97 and ord(char)<=123 or ord(char)>=ord("0") and ord(char)<=ord("9"):
                string+=char
        i=0
        j=len(string)-1
        while(i<j):
            if string[i]!=string[j]:
                return False
            i+=1
            j-=1
        return True