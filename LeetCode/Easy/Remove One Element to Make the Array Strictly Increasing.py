class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        
        for i in range(len(nums)):
            
            if i==0:
                arr=nums[1:]
            else:
                arr=nums[:i]+nums[i+1:]
            
            s=1
            for k in range(1,len(arr)):
                if arr[k-1]<arr[k]:
                    s=s+1
            #print(arr,s)
            if len(arr)==s:
                return True
        
        return False
