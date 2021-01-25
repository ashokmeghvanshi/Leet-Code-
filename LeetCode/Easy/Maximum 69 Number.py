class Solution:
    def maximum69Number (self, num: int) -> int:
        
        def change(num,n):
            t=num
            if t[n]=='9':
                t= t[:n]+'6'+t[n+1:]
            elif t[n]=='6':
                t= t[:n]+'9'+t[n+1:]
            return t
        p=[num]
        
        for i in range(len(str(num))):
            
            res=change(str(num),i)
            p.append(int(res))
        return max(p)
