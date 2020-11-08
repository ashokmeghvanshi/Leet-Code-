class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        b=bin(n)[2:]
        s=0
        for i in range(len(b)-1):
            if b[i]!=b[i+1]:
                s=s+1
        if s==len(b)-1:
            return True
        else:
            return False 
        
