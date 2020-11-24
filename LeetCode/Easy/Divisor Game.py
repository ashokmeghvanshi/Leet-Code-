class Solution:
    def divisorGame(self, N: int) -> bool:
        
        t=N
        k=0
        a,b=0,0
        while t>0:
            for i in range(1,t+1):
                if t%i==0:
                    t=t-i
                    break
            if k%2==0:
                a,b=1,0
            else:
                a,b=0,1
                
            if t==1 and a==1:
                return True
            if t==1 and b==1:
                return False
            
            k=k+1
                
        return False
