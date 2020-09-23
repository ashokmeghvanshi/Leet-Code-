class Solution:
    def numTrees(self, n: int) -> int:

        def fac(n):
            if n==0 or n==1:
                return 1
            result=1
            for i in range(2,n+1):
                result=result*i
            return result
        t=fac(2*n)//(fac(n+1)*fac(n))
        return t
