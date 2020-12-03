class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        s=0
        for i in arr1:
            for j in arr2:
                if abs(i-j)<= d:
                    break
            else:
                s=s+1
        return s
