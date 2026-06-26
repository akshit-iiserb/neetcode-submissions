class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False;

        d={}
        for char in s:
            if char in d:
                d[char]+=1
            else:
                d[char]=1
        for char in t:
            if char in d:
                d[char]-=1
                if d[char]==0:
                    del d[char]
            
        if d=={}:
            return True
        else :
            return False

        