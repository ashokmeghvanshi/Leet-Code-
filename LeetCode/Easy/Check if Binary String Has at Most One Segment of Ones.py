class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        t=0
        for i in range(len(s)-1):
            if s[i]=='1' and s[i+1]=='0' or s[i]=='0' and s[i+1]=='1':
                t=t+1
        if t<=1:
            return True
        return False
