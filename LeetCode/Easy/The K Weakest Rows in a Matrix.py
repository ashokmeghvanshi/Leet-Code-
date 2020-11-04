class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        d={}
        l,res=[],[]
        for i in range(len(mat)):
            d[i]=mat[i].count(1)
            l.append(mat[i].count(1))
        check=sorted(list(dict.fromkeys(l)))
        
        for i in check:
            for j in d:
                if d[j]==i:
                    res.append(j)
                if len(res)==k:
                    return res
