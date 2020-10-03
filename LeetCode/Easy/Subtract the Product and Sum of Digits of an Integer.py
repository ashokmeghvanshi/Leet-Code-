class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro=1
        s=0
        p=n
        while p>0:
            t=p%10
            s=s+t
            pro=pro*t
            p=p//10
        
        return pro-s
