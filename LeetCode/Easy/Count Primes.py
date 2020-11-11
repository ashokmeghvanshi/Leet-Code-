class Solution:
    def countPrimes(self, n: int) -> int:
        
        prime = [True for i in range(n)]
        p = 2
        while(p*p <=n-1):
            if prime[p]==True:
                for i in range( p*p , n,p):
                    prime[i]=False

            p += 1

        s=0
        for x in range(2,len(prime)):
            if prime[x]==True:
                s=s+1
        return s
                
