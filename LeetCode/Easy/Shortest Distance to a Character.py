class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        
        result=[]
        
        for i in range(len(S)):
            t=10000000
            for j in range(i,len(S)):
                if S[j]==C:
                    if t>abs(i-j):
                        t=abs(i-j)
                        break
            
            for k in range(i,-1,-1):
                if S[k]==C:
                    if t>abs(i-k):
                        t=abs(i-k)
                        break
            
            result.append(t)
            
        return result
