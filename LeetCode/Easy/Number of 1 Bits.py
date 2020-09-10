class Solution:
    def hammingWeight(self, n: int) -> int:
        n=int(bin(n)[2:])
        s=0
        while n>0:
            s=s+n%10
            n=n//10
        return s
