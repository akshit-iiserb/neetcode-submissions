class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            dct={}
            for letter in s:
                if letter in dct:
                    dct[letter]+=1
                else:
                    dct[letter]=1
            for letter in t:
                if letter in dct:
                    if dct[letter]==1:
                        del dct[letter]
                    else:
                        dct[letter]-=1
            return dct=={}

        
