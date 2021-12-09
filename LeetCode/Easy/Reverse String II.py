class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        a=list(s)
        
        i=0
        
        while i<len(a):
            a[i:i+k]=a[i:i+k][::-1]
            i=i+2*k
        
        return ''.join(a)
