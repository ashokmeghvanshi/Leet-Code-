class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        
        i=0
        ans=0
        while True and i<len(A[0]):
            t=[]
            for j in A:
                t.append(j[i])
            if t!=sorted(t):
                ans=ans+1
            if i==len(A[0])-1:
                break
            i=i+1
        return ans
                
