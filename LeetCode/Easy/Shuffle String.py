class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        st=''
        for i in range(len(indices)):
            t=indices.index(i)
            st=st+s[t]
            
        return st
            
