import math
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        def gcd(x,y):
            while y:
                x,y=y,x%y
            return x
        
        result=[]
        
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if gcd(i,j)==1:
                    result.append(str(i)+'/'+str(j))
        
        return result
