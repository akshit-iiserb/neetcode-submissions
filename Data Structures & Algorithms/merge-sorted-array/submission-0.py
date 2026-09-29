class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i=0
        j=0
        while(i<m and j<n):
            if nums1[i]>nums2[j]:
                temp=nums1[i]
                nums1[i]=nums2[j]
                nums2[j]=temp
                nums2.sort()
                i+=1
            else:
                i+=1
        while(j<n):
            nums1[m+j]=nums2[j]
            j+=1
    
        
            
                
            

        
