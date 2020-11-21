class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g=sorted(g)
        s=sorted(s)
        
        i,j=0,0
        result=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                
                result = result+1
                i=i+1
            j=j+1
            
        return result
        
