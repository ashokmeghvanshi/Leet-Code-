class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def stoi(s):
            slen=len(s)
            x=0
            for i,n in enumerate(s):
                x=x+(10**(slen - (i+1)) * int(n))
            return x
        return str(stoi(num1)*stoi(num2))
