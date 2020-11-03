class Solution:
    def trailingZeroes(self, n: int) -> int:
        s=1
        for i in range(1,n+1):
            s=s*i
        t=s
        a=0
        while t%10==0:
            t=t//10
            a=a+1
        return a
