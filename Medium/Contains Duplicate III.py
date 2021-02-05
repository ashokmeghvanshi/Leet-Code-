class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        d={}
        for index, num in enumerate(nums):
            if len(d) > 2*t:
                for i in range(num-t, num+t+1):
                    if i in d and index-d[i] <= k:
                        return True
            else:
                for i in d:
                    if abs(num-i) <= t and index-d[i] <= k:
                        return True
            d[num] = index
        return False
