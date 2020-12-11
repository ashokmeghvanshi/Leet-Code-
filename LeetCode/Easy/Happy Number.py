class Solution:
    def isHappy(self, n: int) -> bool:
        
        s=0
        while n!=1:
            t=0
            for i in str(n):
                t=t+int(i)**2
            n=t
            if s==1000:
                break
            s=s+1
        if s==1000 and n!=1:
            return False
        return True
            
