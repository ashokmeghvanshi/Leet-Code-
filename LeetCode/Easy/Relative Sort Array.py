class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        t=sorted(list(dict.fromkeys(arr1)))
        d=[]
        for i in arr2:
            d=d+[i]*arr1.count(i)
        for j in t:
            if j not in d:
                d=d+[j]*arr1.count(j)
        return d
