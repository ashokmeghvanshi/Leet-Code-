class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        partsum, sum1 , count= sum(A)//3, 0,0
        for i in range(len(A)):
            sum1 += A[i]
            if sum1 == partsum:
                count=count+1
                if count>=3:
                    return True
                sum1 = 0
        return False
