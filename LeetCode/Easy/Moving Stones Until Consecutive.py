class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        
        x,y,z=sorted([a,b,c])
        
        min_step=0
        max_step=0
        
        if x == y-1 and y == z - 1:
            min_step = 0
            
        elif y - x > 2 and z - y > 2:
            min_step = 2
        else:
            min_step = 1
            
        max_step = z - x - 2
        
        return [min_step, max_step]
      
        
        
