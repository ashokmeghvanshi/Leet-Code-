class Solution:
    def minimumMoves(self, s: str) -> int:
        
        def change(arr):
            for i in range(len(arr)):
                if arr[i]=='X':
                    arr[i]='O'
            
            return arr
        
        t=list(s)
        ans=0
        i=0
        while i<len(t):
            if t[i]=='X':
                if change(list(t[i:i+3]))!=list(t[i:i+3]):
                    t=t[:i]+change(list(t[i:i+3]))+t[i+3:]
                    ans=ans+1
                    #print(ans,t)
            i=i+1
        return ans
        
        
        
