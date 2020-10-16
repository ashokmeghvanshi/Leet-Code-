class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def check(r,cindex,mat):
            t=0
            for i in range(r):
                if mat[i][cindex]==1:
                    t=t+1
            if t==1:
                return True
            else:
                return False
            
        s=0
        r=len(mat)
        c=len(mat[0])
        for i in range(r):
            if mat[i].count(1)==1:
                cindex=mat[i].index(1)
                if check(r,cindex,mat)==True:
                    s=s+1
        return s
