class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        
        def is_prime(n):
            if n == 1:
                return False
            i = 2
            while i*i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        
        result=0
        for i in range(L,R+1):
            t=bin(i)[2:].count('1')
            if is_prime(t):
                result=result+1
        
        return result
