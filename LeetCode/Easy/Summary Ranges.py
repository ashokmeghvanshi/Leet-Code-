class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        i=0
        
        while i<len(nums):
            t=[]
            t.append(nums[i])
            j=i+1
            p=nums[i]
            while j<len(nums):
                if p+1==nums[j]:
                    t.append(nums[j])
                    p=nums[j]
                else:
                    break
                j=j+1
            if len(t)==1:
                g=str(t[0])
                res.append(g)
                i=i+1
            else:
                i=i+len(t)
                t=sorted(t)
                a=t[0]
                b=t[-1]
                g=str(a)+'->'+str(b)
                res.append(g)
                           
        return res
        
            
            
        
