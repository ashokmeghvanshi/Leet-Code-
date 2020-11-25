class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n%2!=0:
            t=[0]
            if len(t)==n:
                return t
            for i in range(1,n+1):
                t.append(i)
                t.append(-i)
                if len(t)==n and sum(t)==0:
                    return t
        else:
            t=[]
            
            if len(t)==n:
                return t
            for i in range(1,n+1):
                t.append(i)
                t.append(-i)
                if len(t)==n and sum(t)==0:
                    return t
