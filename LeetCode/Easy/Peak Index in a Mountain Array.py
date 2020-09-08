class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_element=max(arr)
        index=arr.index(max_element)
        return index
