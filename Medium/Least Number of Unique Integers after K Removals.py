class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        
        d=dict(sorted(d.items(), key=lambda item: item[1]))
        
        while k>0:
            
            for i in d:
                if k<=0:
                    break
                if d[i]==1:
                    d[i]=d[i]-1
                    k=k-1
            
            if k<=0:
                break
            else:
                for j in d:
                    if d[j]!=0:
                        if k<d[j]:
                            d[j]=d[j]-k
                            k=0
                        else:
                            if d[j]-k<0:
                                k=k-d[j]
                                d[j]=0
                            else:
                                d[j]=d[j]-k
                                k=0
                    if k<=0:
                        break
                
            if k<=0:
                break
    
        res=0
        for i in d:
            if d[i]!=0:
                res=res+1
        
        return res
