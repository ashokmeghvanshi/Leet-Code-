class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
                
        d=list(dict.fromkeys(deck))
        s=[]
        for i in d:
            s.append(deck.count(i))
        
        result=s[0]
        for i in s[1:]:
            result=gcd(result,i)
            
        if result>=2:
            return True
        else:
            return False
