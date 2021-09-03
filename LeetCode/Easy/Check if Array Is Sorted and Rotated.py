class Solution:
    def check(self, nums: List[int]) -> bool:
        
        t=sorted(nums)
        
        if nums==t:
            return True
        
        for i in range(len(t)):
            p=t[i:]+t[:i]
            if p==nums:
                #print(p)
                return True
        return False
