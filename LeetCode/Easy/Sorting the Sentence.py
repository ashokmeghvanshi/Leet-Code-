class Solution:
    def sortSentence(self, s: str) -> str:
        
        s=s.split()
    
        d={}
        
        for i in s:
            d[int(i[-1])]=i[:-1]
        
        key=sorted(d)
        
        ans=''
        for i in key:
            ans=ans+d[i]+' '
        ans=ans[:-1]
        
        return ans
