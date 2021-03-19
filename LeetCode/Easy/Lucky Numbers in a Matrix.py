class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        for i in range(len(matrix)):
            x=min(matrix[i])
            mi=matrix[i].index(x)
            y=-10000000000
            for j in range(len(matrix)):
                if matrix[j][mi]>y:
                    y=matrix[j][mi]
            #print(x,y)
            if x==y:
                return [x]
        return []
