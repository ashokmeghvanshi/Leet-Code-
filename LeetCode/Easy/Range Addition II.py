class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops)==0:
            return n*m
        
        a,b=100000,100000
        for i in ops:
            if i[0]<=a:
                a=i[0]
            if i[1]<=b:
                b=i[1]
        
        return a*b
           
