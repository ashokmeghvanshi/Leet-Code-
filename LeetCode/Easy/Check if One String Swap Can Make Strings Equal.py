class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        i=0
        change=0
        while i<len(s1):
            if s1[i]!=s2[i]:
                change+=1
            i=i+1
        if change==0 or change==2:
            l=list(dict.fromkeys(s1))
            d={}
            for i in s1:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
            p={}
            for i in s2:
                if i not in p:
                    p[i]=1
                else:
                    p[i]+=1
            
            for j in l:
                if j in s2:
                    if d[j]!=p[j]:
                        return False
                else:
                    return False
            return True
        else:
            return False
