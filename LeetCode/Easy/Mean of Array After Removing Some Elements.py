class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        arr=sorted(arr)
        mi,mx=arr[0],arr[-1]
        mi_ct=int(len(arr)*0.05)
        mx_ct=int(len(arr)*0.05)
        arr=arr[mi_ct:-mx_ct]
        s=sum(arr)
        return s/len(arr)
        
