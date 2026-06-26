class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i==len(arr)-1:
                arr[i]=-1
            else:
                 max=arr[i+1]
                 for j in range(i+1,len(arr)):
                     if arr[j]>max:
                         max=arr[j]
                 arr[i]=max
                
        return arr