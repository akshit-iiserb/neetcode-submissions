class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        arr1=[0]*26
        for i in s:
            arr1[ord(i)-97]+=1
        for i in t:
            arr1[ord(i)-97]-=1
        if arr1==[0]*26:
            return True
        else:
            return False
        

            
        
        