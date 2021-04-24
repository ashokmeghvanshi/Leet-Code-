class Solution:
    def maxScore(self, s: str) -> int:
        
        ans=0
        for i in range(len(s)-1):
            t=s[:i+1].count('0')+s[i+1:].count('1')
            if t>ans:
                ans=t
        return ans
