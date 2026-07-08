class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs={}
        for num in nums:
            if num in hs:
                hs[num]+=1
            else:
                hs[num]=1
        lst=[]
        hs=dict(sorted(hs.items(), key=lambda item: item[1]))
        for num in hs:
            lst.append(num)
        
        return lst[-k:]