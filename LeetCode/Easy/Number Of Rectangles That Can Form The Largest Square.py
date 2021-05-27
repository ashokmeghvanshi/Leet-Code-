class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        result=[]
        for i in rectangles:
            result.append(min(i))
        
        mx=max(result)
        return result.count(mx)
