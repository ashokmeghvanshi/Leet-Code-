class Solution:
    def arrangeCoins(self, n: int) -> int:
        a=1
        for i in range(1,n+1):
            n=n-i
            if n<0:
                break
            a=a+1
        return a-1
        
