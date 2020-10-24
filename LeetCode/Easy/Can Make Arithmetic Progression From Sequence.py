class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        s=0
        arr=sorted(arr)
        t=arr[1]-arr[0]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==t:
                s=s+1
        if s==len(arr)-1:
            return True
        else:
            return False
