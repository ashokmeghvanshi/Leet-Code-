class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        l=list(dict.fromkeys(s))
        #print(l)
        
        t=s.count(l[0])
        
        for i in l[1:]:
            if s.count(i)==t:
                pass
            else:
                return False
        
        return True
                
