class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        ts=sum(nums)
        nl=len(nums)-1
        
        result=[abs(ts-nums[0]-(nums[0]*nl))]
        presum=[nums[0]]
        for i in nums[1:]:
            presum.append(presum[-1]+i)
    
        for i in range(1,len(nums)):
            s1=presum[i-1]
            s2=ts-presum[i]
            result.append(abs((i*nums[i]-s1)+(s2-nums[i]*(nl-i))))
            
        return result
            
