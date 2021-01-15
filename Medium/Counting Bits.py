class Solution:
    def countBits(self, num: int) -> List[int]:
        
        dp=[0]*(num+1)
        
        for i in range(num+1):
            t=bin(i)[2:].count('1')
            dp[i]=t
        return dp
