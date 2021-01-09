class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        
        dp=[[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                numsum=0
                for r in range(max(i-K,0), min(i+K+1, len(mat))):
                    for c in range(max(j-K,0), min(j+K+1, len(mat[0]))):
                        numsum=numsum+mat[r][c]
                dp[i][j]=numsum
        return dp
        
