class Solution:
    def maxPower(self, s: str) -> int:
        
        m=1
        for i in range(len(s)-1):
            m1=1
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    m1=m1+1
                    if m1>m:
                        m=m1
                else:
                    break
        return m
                
