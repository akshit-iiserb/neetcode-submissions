class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=[]
        i=0
        j=0
        while(j<len(word1) and i<len(word2)):
            s.append(word1[j])
            s.append(word2[i])
            j+=1
            i+=1
        while(j<len(word1)):
            s.append(word1[j])
            j+=1
        while(i<len(word2)):
            s.append(word2[i])
            i+=1
        
        return "".join(s)
        