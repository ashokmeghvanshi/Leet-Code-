class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        d={}
        dic_len=0
        res=0
        for i in range(1,n+1):
            s=0
            t=i
            while t>0:
                s=s+t%10
                t=t//10
            if s not in d:
                d[s]=[s]
            else:
                d[s].append(i)
                #print(len(d[s]))
            if len(d[s])>dic_len:
                dic_len=len(d[s])
                res=0
            if len(d[s])==dic_len:
                res=res+1
            #print(d,dic_len,res)
        return res
