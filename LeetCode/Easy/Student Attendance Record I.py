class Solution:
    def checkRecord(self, s: str) -> bool:
        
        if s.count('A')<2:
            if len(s)>2:
                t=0
                for i in range(len(s)-2):
                    if s[i]=='L' and s[i+1]=='L' and s[i+2]=='L':
                        return False
                    t=t+1
                if t==len(s)-2:
                    return True
                else:
                    return False
            else:
                if s.count('L')>2:
                    return False
                else:
                    return True
        else:
            return False
