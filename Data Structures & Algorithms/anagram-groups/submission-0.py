class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in range(len(strs)):
            lst=[0]*26
            for j in range(len(strs[i])):
                lst[ord(strs[i][j])-ord('a')]+=1
            res[tuple(lst)].append(strs[i])
        return list(res.values())
        


        
        