class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        s=0
        p=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j:
                    p=p+mat[i][j]

                if i+j==len(mat)-1:
                    s=s+mat[i][j]
        if len(mat)%2==1:
            return s+p- mat[len(mat)//2][len(mat)//2]
        return s+p
