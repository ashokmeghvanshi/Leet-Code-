class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r=len(rowSum)
        c=len(colSum)
        
        result=[[0 for _ in range(c)] for _ in range(r)]
        
        i=0
        while i<r:
            j=0
            while j<c:
                ele=min(rowSum[i],colSum[j])
                result[i][j]=result[i][j]+ele
                rowSum[i]=rowSum[i]-ele
                colSum[j]=colSum[j]-ele
                j=j+1
            i=i+1
            
        return result
