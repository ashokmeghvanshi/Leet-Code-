class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #method 1 
        if target in nums:
            return True
        else:
            return False
        #method two
        ''''if len(nums)==0 or target==None:
            return False
        
        n=sorted(nums)
        if target<n[0]:
            return False
        else:
            for i in n:
                if i==target:
                    return True
                if i>target:
                    return False
            return False'''
