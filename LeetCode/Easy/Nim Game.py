class Solution:
    def canWinNim(self, n: int) -> bool:
        if n > 100000000:
            return n%4 != 0
    
        dp=[False]*(n+1)
        
        def stone(n):
            if dp[n]==True:
                return True
            if n in [1,2,3]:
                return True
            if n%4==0:
                return False
            dp[n]=not(stone(n-1) and stone(n-2) and stone(n-3))
            return dp[n]
        return stone(n)
        
