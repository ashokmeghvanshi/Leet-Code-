class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        s=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if s<1:
                    if i==0:
                        nums[i]=nums[i+1]
                    elif nums[i-1]<=nums[i+1]:
                        nums[i]=nums[i-1]
                    else:
                        nums[i+1]=nums[i]
                    s=s+1
                else:
                    return False            
        return True
    
