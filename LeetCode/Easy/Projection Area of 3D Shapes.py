class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        s=0
        side=0
        for i in grid:
            s=s+i.count(0)
            side=side+max(i)
            
        top=len(grid)*len(grid[0])-s
        #print(top,side)
        
        front=0
        for j in range(len(grid[0])):
            d=-1
            for i in range(len(grid)):
                if grid[i][j]>d:
                    d=grid[i][j]
            front=front+d
        return top+front+side
