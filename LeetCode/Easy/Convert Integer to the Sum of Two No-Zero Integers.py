class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        p=n
        t=n-1
        q=p-t
        while '0' in str(n) or '0' in str(t) or '0' in str(q):
            n=n-1
            t=n
            q=p-t
        return [q,t]
