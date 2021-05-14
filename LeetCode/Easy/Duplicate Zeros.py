class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while i<len(arr):
            if arr[i]==0:
                j=i+1
                pre=arr[i]
                while j<len(arr):
                    nxt=arr[j]
                    arr[j]=pre
                    pre=nxt
                    j=j+1
                i=i+2
            else:
                i=i+1
                #print(arr,i)
        
