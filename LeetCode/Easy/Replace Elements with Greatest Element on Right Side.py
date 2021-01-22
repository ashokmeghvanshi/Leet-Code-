class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        t=[]
        for i in range(len(arr)-1):
            maxlast=max(arr[i+1:])
            t.append(maxlast)
        t.append(-1)
        return t
            
