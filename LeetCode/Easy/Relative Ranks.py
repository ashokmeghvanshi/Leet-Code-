class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        l=sorted(nums)[::-1]
        result=[]
        #print(l)
        for i in nums:
            if l.index(i)==0:
                result.append('Gold Medal')
            elif l.index(i)==1:
                result.append('Silver Medal')
            elif l.index(i)==2:
                result.append('Bronze Medal')
            else:
                result.append(str(l.index(i)+1))
        return result