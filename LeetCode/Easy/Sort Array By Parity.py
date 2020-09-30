class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        a,b=[],[]
        for i in A:
            if i%2==0:
                a.append(i)
            else:
                b.append(i)
        return a+b
