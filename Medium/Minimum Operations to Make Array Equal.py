class Solution:
    def minOperations(self, n: int) -> int:
        arr=[((2*i)+1) for i in range(n)]
        tar=sum(arr)//n
        result=0
        for i in arr:
            if i<tar:
                result=result+tar-i
            else:
                break
        return result
