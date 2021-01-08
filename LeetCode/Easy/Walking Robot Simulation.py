class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obstacles = {(x, y) for x, y in obstacles}
        
        result=0
        a,b=0,0
        dx,dy=0,1
        for i in commands:
            if i==-1:
                dx,dy=dy,-dx 
            elif i==-2:
                dx,dy=-dy,dx
            else:
                for j in range(i):
                    if (a+dx,b+dy) in obstacles:
                        break
                    a,b=a+dx,b+dy
                
                result=max(result,a*a+b*b)
        
        return result
    
