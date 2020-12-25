class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        d=[1]
        u=[1]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                u.append(d[i-1]+1)
                d.append(d[i-1])
            elif nums[i]<nums[i-1]:
                d.append(u[i-1]+1)
                u.append(u[i-1])
            else:
                d.append(d[i-1])
                u.append(u[i-1])
        return max(d[-1],u[-1])
            
