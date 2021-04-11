class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        d={}
        ss='abcdefghijklmnopqrstuvwxyz'
        for i in range(26):
            d[ss[i]]=widths[i]
        #print(d)
        ans=[]
        t=0
        res=''
        i=0
        while i<len(s):
            if t+d[s[i]]<=100:
                t=t+d[s[i]]
                res=res+s[i]
                i=i+1
            else:
                ans.append(res)
                res=''
                t=0
                
            #print(res,t,ans)
        ans.append(res)
        return [len(ans),t]
                
