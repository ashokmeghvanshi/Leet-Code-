class Solution:
    def maximumTime(self, time: str) -> str:
        
        t=list(time)
        #print(t)
        if t[0]=='?':
            if t[1] in ['0','1','2','3']:
                t[0]='2'
            elif t[1] in ['4','5','6','7','8','9']:
                t[0]='1'
            else:
                t[0]='2'
        if t[1]=='?':
            if t[0]=='0' or t[0]=='1':
                t[1]='9'
            else:
                t[1]='3'
        if t[3]=='?':
            t[3]='5'
        if t[4]=='?':
            t[4]='9'
        ans=''.join(t)
        return ans
