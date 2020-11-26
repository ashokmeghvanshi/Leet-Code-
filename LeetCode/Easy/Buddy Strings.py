class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if A is None or B is None or len(A)!=len(B):
            return False
        
        d1,d2=-1,-1
        t=set()
        for i in range(len(A)):
            if A[i]!=B[i]:
                if d1==-1:
                    d1=i
                elif d2==-1:
                    d2=i
                else:
                    return False
            t.add(A[i])
    
        if d1 != -1 and d2 != -1:
            return A[d1] == B[d2] and A[d2] == B[d1]
        if d1 != -1:
            return False
        return len(t) < len(A) 
    
            
