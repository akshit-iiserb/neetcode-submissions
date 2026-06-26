class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        for i in range(len(strs[0])):
            for str in strs:
                if len(str)==i or str[i]!=strs[0][i]:
                    return strs[0][:i]
        return strs[0]
            
        