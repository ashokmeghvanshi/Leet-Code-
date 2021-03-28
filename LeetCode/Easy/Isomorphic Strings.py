class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        d={}
        c={}
        for i in range(len(s)):
            d[s[i]]=t[i]
            c[t[i]]=s[i]
        #print(c,d)
        for i in range(len(s)):
            if d[s[i]]!=t[i] or c[t[i]]!=s[i]:
                return False
        return True
