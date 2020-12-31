class Solution:
    def maximumSwap(self, num: int) -> int:
        
        res=[num]
        t=list(str(num))
        
        for i in range(len(t)-1):
            for j in range(i+1,len(t)):
                t[i],t[j]=t[j],t[i]
                if int(''.join(t))>res[-1]:
                    res.append(int(''.join(t)))
                t[j],t[i]=t[i],t[j]
        return max(res)
            
        
