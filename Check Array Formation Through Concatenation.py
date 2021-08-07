class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        ans=[]
        c=0
        for i in arr:
            for j in pieces:
                if i in j:
                    ans=ans+j
                    pieces.remove(j)
                    c=1
            
            if c==0:
                return False
            #print(ans)
        if ans==arr:
            return True
        else:
            return False
