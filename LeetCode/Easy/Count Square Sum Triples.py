class Solution:
    def countTriples(self, n: int) -> int:
        
        nums=[]
        for i in range(1,n+1):
            nums.append(i**2)
        
        #print(nums)
        
        ans=0
        
        for i in nums:
            for j in nums:
                if i+j in nums:
                    ans=ans+1
#         for i in nums:
#             for j in nums:
#                 if ((i**2)+(j**2))**(0.5) in nums:
#                     ans=ans+1
        
        return ans
                
