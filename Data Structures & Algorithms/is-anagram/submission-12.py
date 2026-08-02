class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            hs=[0]*26
            for i in range(len(s)):
                hs[ord(s[i])-ord("a")]+=1
                hs[ord(t[i])-ord("a")]-=1
        return hs==[0]*26
        