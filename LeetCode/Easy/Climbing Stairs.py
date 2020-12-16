class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=2
        
        if n==1:
            return dp[n-1]
        else:
            for i in range(2,n+1):
                dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n-1]
