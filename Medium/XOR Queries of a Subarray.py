class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        dp=[0]
        
        for i in arr:
            dp.append(dp[-1]^i)
        #print(dp)
        res=[]
        for i in queries:
            l=i[0]
            r=i[1]
            res.append(dp[l]^dp[r+1])
        return res  
