class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a=set()
        for i in nums:
            a.add(i)
        t=[]
        for i in range(1,len(nums)+1):
            if i not in a:
                t.append(i)
        return t
        
