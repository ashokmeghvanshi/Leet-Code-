class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        
        mi=min(A)+K
        mx=max(A)-K
        
        if mx-mi>=0:
            return mx-mi
        else:
            return 0
