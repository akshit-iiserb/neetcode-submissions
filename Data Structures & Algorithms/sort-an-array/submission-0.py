class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,start,mid,end):
            n1=mid-start+1
            n2=end-mid
            L=[0]*n1
            R=[0]*n2
            for i in range(n1):
                L[i]=arr[start+i]
            for j in range(n2):
                R[j]=arr[mid+j+1]
            i=0
            j=0
            k=start
            while(i<n1 and j<n2):
                if(L[i]>R[j]):
                    arr[k]=R[j]
                    j+=1
                else:
                    arr[k]=L[i]
                    i+=1
                k+=1
            
            while(i<n1):
                arr[k]=L[i]
                i+=1
                k+=1
            while(j<n2):
                arr[k]=R[j]
                j+=1
                k+=1
        def mergesort(arr,start,end):
            if start<end:
                mid=(start+end)//2
                mergesort(arr,start,mid)
                mergesort(arr,mid+1,end)
                merge(arr,start,mid,end)

        start=0;
        end=len(nums)-1
        mergesort(nums,start,end)
        return nums

                
        