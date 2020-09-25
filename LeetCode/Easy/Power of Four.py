class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        for i in range(num+1):
            if 4**i==num:
                return True
            if 4**i>num:
                return False
        return False
