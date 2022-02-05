class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        ans=0
        
        for i in range(len(s)-2):
            t=s[i:i+3]
            c1,c2=t[0],t[1]
            if t.count(c1)==1 and t.count(c2)==1:
                ans=ans+1
                
        return ans
