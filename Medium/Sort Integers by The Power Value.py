class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        interval={}
        for i in range(lo,hi+1):
            t=i
            s=0
            while t!=1:
                if t%2==0:
                    t=t//2
                else:
                    t=t*3+1
                s=s+1
            interval[i]=s
        interval=dict(sorted(interval.items(), key=lambda item: item[1]))
        new_k=list(interval)[k-1]
        return new_k
        
                    
            
