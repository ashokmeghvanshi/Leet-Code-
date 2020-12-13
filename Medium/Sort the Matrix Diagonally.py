class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        sr=len(mat)
        sc=len(mat[0])
        
        res=[[0 for _ in range(sc)] for _ in range(sr)]
        i=sr-1
        
        while i>-1:
            t=[]
            k=i
            j=0
            while k<sr and j<sc:
                t.append(mat[k][j])
                k=k+1
                j=j+1
                
            t=sorted(t)
            k=i
            j=0
            x=0
            while k<sr and j<sc:
                res[k][j]=t[x]
                k=k+1
                j=j+1
                x=x+1
                
            i=i-1
        
        j=1
        while j<sc:
            t=[]
            k=j
            i=0
            while i<sr and k<sc:
                t.append(mat[i][k])
                i=i+1
                k=k+1
                
            t=sorted(t)
            k=j
            i=0
            x=0
            while k<sc and i<sr:
                res[i][k]=t[x]
                k=k+1
                i=i+1
                x=x+1
                
            j=j+1
        return res
