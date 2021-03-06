class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        l=[x for x in range(len(S)+1)]
        a,b=0,len(S)
        res=[]
        
        for j in range(len(S)):
            if S[j]=='I':
                res.append(l[a])
                a=a+1
                
            elif S[j]=='D':
                res.append(l[b])
                b=b-1
        res.append(l[a])    
        return res
                
