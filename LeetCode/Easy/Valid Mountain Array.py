class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)==1 or len(A)==0 or len(A)==2:
            return False
        mi=A.index(max(A))
        if mi==len(A)-1 or mi==0:
            return False
        s1=0
        for i in range(mi):
            if A[i]<A[i+1]:
                s1=s1+1
            else:
                return False
        #print('s1',s1)
        s1=s1+1
        #print('s2',s1)
        for i in range(mi,len(A)-1):
            if A[i]>A[i+1]:
                s1=s1+1
            else:
                return False
        #print(mi,s1)
        if s1==len(A):
            return True
        else:
            return False
