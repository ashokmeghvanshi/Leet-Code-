class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        i=len(matrix)-1
        while i>0:
            j=1
            while j<len(matrix[0]):
                #print(matrix[i][j],matrix[i-1][j-1])
                if matrix[i][j]==matrix[i-1][j-1]:
                    pass
                else:
                    return False
                j=j+1
            #print('\n')
            i=i-1
        return True
                    
