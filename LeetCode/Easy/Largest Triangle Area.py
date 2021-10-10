class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        ans=-1
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(i+2,len(points)):
                    x1,y1=points[i]
                    x2,y2=points[j]
                    x3,y3=points[k]
                    t=abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
                    if t>ans:
                        ans=t
        return ans
    

