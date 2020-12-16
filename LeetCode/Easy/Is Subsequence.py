class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=='':
            return True
        a=0
        for i in range(len(s)):
            #print(i,s[i],a,t)
            if s[i] in t and i==0:
                a=t.index(s[i])
                t=t[a+1:]
            elif s[i] in t:
                a=t.index(s[i])
                t=t[a+1:]
            else:
                return False
            
        return True
    
    
