class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        d=[[0 for i in range(m)]for j in range(n)]
        for i in indices:
            r=int(i[0])
            c=int(i[1])
            for j in range(len(d[r])):
                d[r][j]=d[r][j]+1
            for k in range(n):
                d[k][c]=d[k][c]+1
        s=0
        for i in d:
            for j in i:
                if j%2!=0:
                    s=s+1
        return s
            
