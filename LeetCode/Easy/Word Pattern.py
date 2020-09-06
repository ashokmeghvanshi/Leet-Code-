class Solution:
    def wordPattern(self, pattern: str, str1: str) -> bool:

        t=[]
        for i in str1.split(' '):
            t.append(i)

        if len(pattern)!=len(t):
            return False
        d={}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if t[i] not in d.values():
                    d[pattern[i]]=t[i]
                    #print(i,d)
                else:
                    return False
            else:
                if d[pattern[i]]!=t[i]:
                    return False
        
        return True 
