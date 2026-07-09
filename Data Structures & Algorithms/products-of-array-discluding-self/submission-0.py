class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[]
        lst=nums.copy()
        for i in range(len(lst)):
            lst=nums.copy()
            lst.pop(i)
            pdt=1
            for j in range(len(lst)):
                pdt*=lst[j]
            product.append(pdt)
        return product
                
            
        
        