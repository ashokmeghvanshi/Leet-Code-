class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        check=A[0]
        result=[]
        
        for i in check:
            s=0
            mi=10000000
            for j in A:
                if i in j:
                    s=s+1
                    k=j.count(i)
                    #print('k',k)
                    if k<mi:
                        mi=k
            #print(i,s,mi)
            if s==len(A) and result.count(i)!=mi:
                for l in range(mi):
                    result.append(i)
        return result
            
