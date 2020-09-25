class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(n+1):
            if 2**i==n:
                return True
            if 2**i>n:
                return False
        return False
