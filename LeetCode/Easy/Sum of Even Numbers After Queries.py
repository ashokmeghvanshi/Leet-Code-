class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        
        result=[]
        s=0
        for i in A:
            if i%2==0:
                s=s+i
        #print(s)
        for i in range(len(queries)):
            val = queries[i][0]
            index = queries[i][1]
            t=A[index]
            A[index]=A[index]+val
            
            if t%2==0 and A[index]%2!=0:
                result.append(s-t)

            elif t%2!=0 and A[index]%2==0:
                result.append(s+A[index])
            
            elif t%2==0 and A[index]%2==0:
                result.append(s+val)
            else:
                result.append(s)
            s=result[-1]
        return result

            
            
            
            
            
