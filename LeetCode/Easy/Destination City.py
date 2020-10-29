class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d={}
        a={}
        for i in paths:
            for j in i:
                if j not in d:
                    d[j]=1
                    a[j]=i.index(j)
                else:
                    d[j]=d[j]+1
                    a[j]=i.index(j)
                    
        for i,j in zip(d,a):
            if d[i]==1 and a[j]==1:
                return i
        
