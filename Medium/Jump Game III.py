class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def dfs(arr1,s1,start1):
            #print(arr1,start1,s1)
            if start1<0 or start1>=len(arr1):
                return False
            if arr1[start1]==0:
                return True
            if start1 in s1:
                return False
            
            s1.add(start1)
            return dfs(arr1,s1,start1+arr1[start1]) or dfs(arr1,s1,start1-arr1[start1])
            
        
        s=set()
        return dfs(arr,s,start)
