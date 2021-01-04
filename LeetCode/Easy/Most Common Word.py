class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph1=''
        for i in paragraph:
            if i not in ['!','?',',',';','.',str("'")]:
                paragraph1=paragraph1+i
            else:
                paragraph1=paragraph1+' '
        #print(paragraph1)
        d={}
        for i in paragraph1.split():
            t=i.lower()
            if t not in d and t not in banned:
                d[t]=1
            else:
                if t in d and t not in banned:
                    d[t]=d[t]+1
        f,f1=0,0
        #print(d)
        for i in d.values():
            if i==max(d.values()):
                f=f+1
            f1=f1+1
        if f1==f:
            z=sorted(d.keys())
            g={}
            for i in z:
                g[i]=d[i]
            #print(g)
            s=max(g, key=g.get)
            return s
        else:
            s=max(d, key=d.get)
            return s
