class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n==0:
            return 0
        
        s=0
        result=[0]*(n+1)
        result[1]=1
        i=1
        while s+2!=n+1:
            result[2*i]=result[i]
            #print(result,s)
            s=s+1
            if s+2==n+1:
                break
            result[2*i+1]=result[i]+result[i+1]
            #print(result,s)
            s=s+1
            if s+1==n+1:
                break
            i=i+1
            #print(result,s)
        return max(result)
