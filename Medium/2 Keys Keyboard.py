class Solution:
    def minSteps(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[1]=2
        
        for i in range(2,n):
            ld=0
            for j in range(i-1,0,-1):
                if (i+1)% j == 0:
                    ld=j
                    break
            if ld==0:
                dp[i]=i+1  
            else:
                dp[i]=dp[ld-1]+(i+1)//ld
        
        return dp[-2]
    
         
