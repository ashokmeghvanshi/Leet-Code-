class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        res=[]
        for i in points:
            res.append(i[0])
        
        s=0
        res=sorted(res)
        for i in range(len(res)-1):
            s=max(s,res[i+1]-res[i])
        return s
        
        ''''result=0
        points=sorted(points)
        for i in range(len(points)-1):
            result=max(result,points[i+1][0]-points[i][0])
        return result'''
