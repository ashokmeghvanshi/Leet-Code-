class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        x=1
        while True:
            t=0
            a=x
            for i in nums:
                #print(x,i)
                y=a+i
                if y>=1:
                    t=t+1
                    a=y
                else:
                    break
            #print(t,i,x,y)
                
            if t==len(nums):
                return x
            else:
                x=x+1
