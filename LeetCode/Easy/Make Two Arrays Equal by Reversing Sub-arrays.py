class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        t=sorted(target)
        a=sorted(arr)
        if a==t:
            return True
        return False
