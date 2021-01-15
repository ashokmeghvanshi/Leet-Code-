class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix[0])
        m = len(matrix)
        
        dp = [[0]*(n+1) for i in range(m+1)]
        #print(dp)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == 0:
                    dp[i][j]=0
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
        #print(dp)
        
        result=0
        
        for i in range(m+1):
            for j in range(n+1):
                result = result + dp[i][j]
                
        return result
