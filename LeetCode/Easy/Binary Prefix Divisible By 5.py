class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        
        s=''
        res=[]
        for i in A:
            s=s+str(i)
            n=int(s,2)
            #print(s,n)
            if n%5==0:
                res.append(True)
            else:
                res.append(False)
        return res
