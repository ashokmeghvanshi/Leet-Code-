class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(n):
            nums.append(start+2*i)
        if n==1:
            return nums[0]
        a=nums[0]
        b=nums[1]
        t=a^b
        for i in nums[2:]:
            t=t^i
        return t
        
