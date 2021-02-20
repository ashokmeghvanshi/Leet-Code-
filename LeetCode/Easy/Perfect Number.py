class Solution:
    def checkPerfectNumber(self, nums: int) -> bool:
        if nums<=1:
            return False
        s=1
        for i in range(2,int(nums**0.5)+1):
            if nums%i==0:
                s=s+i+nums//i
        if s==nums:
            return True
        else:
            return False
        
                
