class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        
        res=[]
        d={}
        for r in range(R):
            for c in range(C):
                dis=abs(c0-c)+abs(r0-r)
                if dis not in d:
                    d[dis]=[[r,c]]
                else:
                    d[dis].append([r,c])
                    
        for i in sorted(d):
            res=res+d[i]
        return res
