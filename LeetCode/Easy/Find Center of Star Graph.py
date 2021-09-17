class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        d={}
        for i in edges:
            a,b=i[0],i[1]
            if a not in d:
                d[a]=1
            else:
                d[a]=d[a]+1
            
            if b not in d:
                d[b]=1
            else:
                d[b]=d[b]+1
        
        #print(d)
        mx=max(d.values())
        #print(mx)
        
        for i in d:
            if d[i]==mx:
                return i
        
