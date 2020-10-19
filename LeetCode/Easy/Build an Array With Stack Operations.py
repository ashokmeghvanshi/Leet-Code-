class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        res=[]
        reftarget=[]
        for i in range(1,n+1):
            if i in target:
                res.append('Push')
                reftarget.append(i)
            else:
                res.append('Push')
                res.append('Pop')
            if reftarget==target:
                return res
            
                
