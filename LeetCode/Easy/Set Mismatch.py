class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        setsum=0
        res=[]
        miss=[]
        for i in nums:
            if i not in miss:
                setsum=setsum+i
                miss.append(i)
        
        res.append(sum(nums)-setsum)
        
        m=0
        for i in range(1,len(nums)+1):
            m=m+i
        
        res.append(m-setsum)
            
        return res
    
