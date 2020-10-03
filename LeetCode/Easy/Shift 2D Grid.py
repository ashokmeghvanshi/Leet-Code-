class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r=len(grid)
        c=len(grid[0])
        if k%(r*c)==0:
            return grid
        a=k%(r*c)
        #print(a)
        d=[]
        for i in grid:
            d=d+i
        t=d[-a:]+d[:-a]
        #print(t)
        i=0
        p=[]
        while i<r*c:
            p.append(t[i:i+c])
            i=i+c
        return p
        
