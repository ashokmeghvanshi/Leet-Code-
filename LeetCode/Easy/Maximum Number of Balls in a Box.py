class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        def check(n):
            s=0
            while n>0:
                s=s+n%10
                n=n//10
            return s
        
        box={}
        ans=-1000000
        for i in range(lowLimit,highLimit+1):
            t=check(i)
            if t not in box:
                box[t]=1
            else:
                box[t]+=1
            if box[t]>ans:
                ans=box[t]
        #print(dict(sorted(box.items(), key=lambda x: x[0])))
        return ans
