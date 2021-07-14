class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        t=sorted(A)
        i=0
        while i<K:
            if t[i]<0:
                t[i]=-t[i]
            
            elif t[i]==0:
                break
            else:
                mi=t.index(min(t))
                t[mi]=-t[mi]
                
            i=i+1
            
        return sum(t)
