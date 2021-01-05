class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        R=len(grid)
        C=len(grid[0])
        cost=grid
        tc = [[0 for x in range(C)] for x in range(R)] 
        tc[0][0] = cost[0][0]
        
        for i in range(1, R): 
            tc[i][0] = tc[i-1][0] + cost[i][0]
        
        for j in range(1, C): 
            tc[0][j] = tc[0][j-1] + cost[0][j]
        
        for i in range(1, R): 
            for j in range(1, C): 
                tc[i][j] = min(tc[i-1][j], tc[i][j-1]) + cost[i][j]
                
        return tc[R-1][C-1] 
        
