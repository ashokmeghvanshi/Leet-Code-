class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        s=float('inf')
        p=sorted(arr)
        res=[]
        for i in range(len(p)-1):
            
            if abs(p[i]-p[i+1])==s:
                res.append([p[i],p[i+1]])
            
            elif abs(p[i]-p[i+1])<s:
                s=abs(p[i]-p[i+1])
                
                res=[[p[i],p[i+1]]]
        return res
    
