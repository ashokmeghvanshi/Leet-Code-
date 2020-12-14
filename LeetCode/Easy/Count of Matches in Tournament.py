class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        tm=0
        
        while n>0:
            if n<2:
                break
            elif n%2==0:
                tm=tm+n//2
                n=n//2
            else:
                tm=tm+(n-1)//2
                n=((n-1)//2)+1
            #print(n,tm)
            
        return tm
