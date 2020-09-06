class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        s=''
        for i in A:
            s=s+str(i)
        c=K+int(s)
        return list(str(c))
