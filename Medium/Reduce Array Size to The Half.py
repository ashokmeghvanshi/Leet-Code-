class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        hl=len(arr)//2
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        #print(d)
        result=[]
        d=dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
        s=1
        for i in d:
            #print(d[i],hl)
            if d[i]==hl:
                return s
            elif d[i]<hl:
                hl=hl-d[i]
                s=s+1
        return s 
