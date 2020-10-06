class Solution:
    def checkStraightLine(self, co: List[List[int]]) -> bool:
        x1=co[0][0]
        y1=co[0][1]
        x2=co[1][0]
        y2=co[1][1]
        dy=(y2-y1)
        dx=(x2-x1)
        
        for i in range(len(co)):
            x=co[i][0]
            y=co[i][1]
            if dx*(y-y1)!=dy*(x-x1):
                return False
        return True
        
                
            
