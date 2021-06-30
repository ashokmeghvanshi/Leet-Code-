class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        minindex=1000000000000
        mindistance=100000000000
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                d=abs(points[i][0]-x)+abs(points[i][1]-y)
                if d<mindistance:
                    mindistance=d
                    minindex=i
                        
                #print(points[i],i,d,mindistance,minindex)
        if minindex!=1000000000000:
            return minindex
        
        return -1
