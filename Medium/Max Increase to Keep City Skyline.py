class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        tb=[]
        lr=[]
        for i in grid:
            lr.append(max(i))
        
        j=0
        while j<len(grid[0]):
            i=0
            mxe=0
            while i<len(grid):
                if mxe<grid[i][j]:
                    mxe=grid[i][j]
                i=i+1
            j=j+1
            tb.append(mxe)
        
        result=0
        for i in range(len(tb)):
            for j in range(len(lr)):
                result=result+min(tb[i],lr[j])-grid[i][j]
        return result
                
