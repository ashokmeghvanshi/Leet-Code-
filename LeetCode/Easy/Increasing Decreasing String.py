class Solution:
    def sortString(self, s: str) -> str:
        l={}
        for i in s:
            if i not in l:
                l[i]=1
            else:
                l[i]=l[i]+1
        st=''
        for i in sorted(l.keys()):
            st=st+i
        res=''
        i=0
        a=0
        while len(res)!=len(s):
            
            if i<len(s) and a==0:
                if l[st[i]]>0:
                    res=res+st[i]
                    l[st[i]]=l[st[i]]-1
                i=i+1
                
                if i==len(st):
                    a=1
                    i=i-1
                    
            elif i>-1 and a==1:
                if l[st[i]]>0:
                    res=res+st[i]
                    l[st[i]]=l[st[i]]-1   
                i=i-1
                if i==-1:
                    a=0
                    i=i+1
        return res
