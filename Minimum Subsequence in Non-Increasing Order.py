class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        t_sum=sum(nums)
        
        t=sorted(nums)
        s=0
        ans=[]
        for i in t[::-1]:
            
            #print(s,t_sum)
            ans.append(i)
            t_sum=t_sum-i
            s=s+i
            
            if s>t_sum:
                return ans
            
    
            
