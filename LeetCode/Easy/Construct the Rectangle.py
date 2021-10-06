class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        def root(a):
            t=a**(0.5)
            if str(t)[-2:]=='.0':
                    return True
            
            return False
        
        if root(area)==True:
            return [int(area**(0.5)),int(area**(0.5))]
        
        #ans=[[-1,-1],[10000000000000000000]]
        
        for L in range(1,area+1):
            W=area//L
            if L>=W and L*W==area:
                # if abs(L-W)<ans[1][0]:
                #     ans[0]=[L,W]
                #     ans[1]=[abs(L-W)]
                #     #print(ans)
                return [L,W]
