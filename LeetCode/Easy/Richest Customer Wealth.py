class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max_w=0
        
        for i in accounts:
            t=sum(i)
            if t>max_w:
                max_w=t
        return max_w
