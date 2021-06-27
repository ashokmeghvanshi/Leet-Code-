class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<11:
            return []
        
        res=[]
        i=0
        x={}
        while i<len(s)-9:
            t=s[i:i+10]
            if t not in x:
                x[t]=1
            else:
                x[t]=x[t]+1
            i=i+1
        
        for i in x:
            if x[i]>1:
                res.append(i)
        return res
    
