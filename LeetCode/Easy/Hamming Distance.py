class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        x,y=bin(x)[2:],bin(y)[2:]
        
        x='0'*(32-len(x))+x
        y='0'*(32-len(y))+y
        
        c=0
        for i in range(32):
            if x[i]!=y[i]:
                c=c+1
        return c
