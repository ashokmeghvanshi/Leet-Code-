class Solution:
    def totalMoney(self, n: int) -> int:
        
        result=0
        m,s=1,8
        t=0
        while True:
            for i in range(m,s):
                if t!=n:
                    result=result+i
                    t=t+1
                else:
                    break
                
            if n==t:
                break
            else:
                m=m+1
                s=s+1
        return result
