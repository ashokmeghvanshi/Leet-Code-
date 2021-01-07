class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n=len(triangle)
        dp=[[0 for _ in range(n)] for _ in range(n)]
        
        dp[0][0]=triangle[0][0]
        
        for i in range(1,n):
            m=len(triangle[i])
            for j in range(m):
                if j==0:
                    dp[i][j]=dp[i-1][j]+triangle[i][j]
                elif j==m-1:
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
                    
        return min(dp[-1])
    
