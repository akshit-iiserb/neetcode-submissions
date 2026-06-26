class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        for i in range(len(t)):
            if t[i] in d:
                d[t[i]]-=1
                if d[t[i]]==0:
                    del d[t[i]]
            else:
                return False
        return d=={}
        
        