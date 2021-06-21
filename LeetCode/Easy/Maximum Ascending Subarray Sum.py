class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        ans=nums[0]
        
        i=0
        while i<len(nums):
            a=nums[i:i+1]
            if a[0]>ans:
                ans=a[0]
            #print(a)
            for j in range(i+1,len(nums)):
                if nums[j]>a[-1]:
                    a=a+[nums[j]]
                    #print(a,i)
                    t=sum(a)
                    if t>ans:
                        ans=t
                    if j==len(nums)-1:
                        i=j+1
                else:
                    i=j
                    if j==len(nums)-1:
                        i=j+1
                    break
        return ans
