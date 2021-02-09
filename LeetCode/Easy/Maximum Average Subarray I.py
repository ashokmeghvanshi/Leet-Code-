class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        s=sum(nums[:k])
        res=s
        for i in range(1,len(nums)-k+1):
            s=s-nums[i-1]+nums[k+i-1]
            if s>res:
                res=s
            
        return res/k
            
        
