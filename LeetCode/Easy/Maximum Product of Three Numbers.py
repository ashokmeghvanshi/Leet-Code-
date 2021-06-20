class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        t=sorted(nums)
        #print(t)
        
        a,b,c=t[-3],t[-2],t[-1]
        p,q=t[0],t[1]
        
        #print(a,b,c,p,q)
        ans=[a*b*c,p*q*c]
        #print(ans)
        return max(ans)
