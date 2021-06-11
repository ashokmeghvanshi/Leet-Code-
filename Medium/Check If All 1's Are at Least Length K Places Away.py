class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        onei=[]
        for i in range(len(nums)):
            if len(onei)==0 and nums[i]==1:
                onei.append(i)
            elif nums[i]==1:
                if (i-onei[-1])-1>=k:
                    onei.append(i)
                else:
                    return False
            
        if len(onei)==nums.count(1):
            return True
        return False
    
