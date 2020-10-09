class Solution:
    def thousandSeparator(self, n: int) -> str:
        s=str(n)[::-1]
        if len(s)<4:
            return str(n)
        t=''
        p=''
        for i in s:
            p=p+i
            if len(p)==3:
                t=t+p+'.'
                p=''
        t=t+p
        if t[-1]=='.':
            t=t[:-1]
        return t[::-1]
            
        
