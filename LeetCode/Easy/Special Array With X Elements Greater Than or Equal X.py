class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        t=sorted(nums)[::-1]
        
        for i in range(len(nums)+1):
            s=0
            for j in t:
                if j>=i:
                    s=s+1
                else:
                    break
            if s==i:
                return i
        return -1
