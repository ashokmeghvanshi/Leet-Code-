class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        t=[]
        for i in range(left,right+1):
            if i<10:
                t.append(i)
            else:
                a=i
                l=len(str(a))
                s=0
                while i>0:
                    m=i%10
                    if m!=0 and a%m==0:
                        s=s+1
                    i=i//10
                if s==l:
                    t.append(a)
        return t
                    
                    
