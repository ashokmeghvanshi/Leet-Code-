class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        x,y=min(nums),max(nums)
        
        def check(a,b):
            
            while a!=b:
                if a>b:
                    a=a-b
                else:
                    b=b-a
            return a
        
        return check(x,y)
