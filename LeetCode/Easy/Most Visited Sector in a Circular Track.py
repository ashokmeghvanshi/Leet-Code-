class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        
        t=[]
        d={}
        
        for i in range(1,n+1):
            t.append(i)
            d[i]=0
        #print(t,d)
        
        laststep=0
        for j in range(1,len(rounds)):
            
            if rounds[j-1]<=rounds[j]:
                
                s=rounds[j-1]
                
                if s==laststep:
                    s=s+1
                for k in range(s,rounds[j]+1):
                    d[k]=d[k]+1
                
                laststep=rounds[j]
            
            else:
                s=rounds[j-1]
                
                if s==laststep:
                    s=s+1
                
                for k in range(s,n+1):
                    d[k]=d[k]+1
                
                for k in range(1,rounds[j]+1):
                    d[k]=d[k]+1
                
                laststep=rounds[j]
            
            #print(rounds[j-1],rounds[j],d)
        
        mx=max(d.values())
        
        #print(mx)
        
        ans=[]
        for i in d:
            if d[i]==mx:
                ans.append(i)
        
        return ans
