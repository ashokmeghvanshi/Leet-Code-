class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if x<0:
            sign=-1
            x=-x
        
        t=int(str(x)[::-1])

        if t<-(2**31) or t>2**31 -1:
            return 0
        else:
            if sign==-1:
                return -t
            else:
                return t
        
            
            
