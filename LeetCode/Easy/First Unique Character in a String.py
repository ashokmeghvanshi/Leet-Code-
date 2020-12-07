class Solution:
    def firstUniqChar(self, s: str) -> int:
        t=[]
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in t:
                return i
            else:
                t.append(s[i])
        return -1
