class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        time=0
        x,y=points[0][0],points[0][1]

        for i in points[1:]:
            a,b=i[0],i[1]
            time=time+max(abs(x-a),abs(y-b))
            x,y=a,b
        return time
