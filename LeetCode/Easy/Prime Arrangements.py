class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        
        def is_prime(n):
            
            if n == 1:
                return False

            i = 2
            while i*i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True

        non_prime=0
        prime=0
        for i in range(1,n+1):
            if is_prime(i)==True:
                prime=prime+1
            else:
                non_prime=non_prime+1
        
        def fac(t):
            result=1
            for i in range(2,t+1):
                result=result*i
            return result
        
        ans=(fac(non_prime)*fac(prime))%(10**9+7)
        return ans
        
        # Because we have restricted that the prime number can only do permutation on         #their own position
		
        # So as for those numbers as not prime. For example, for number 5, we have 
		# * 2 none prime number (1, 4) 
		# * 3 prime number (2, 3, 4)
		# So there is 2! permutation possibilities for none prime number 
		# and 3! permutation possibilities for prime number which total give us
		# 2! * 3! permutation possibilities.
