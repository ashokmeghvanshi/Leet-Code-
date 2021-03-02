class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack=[]
        mx=0
        t=0
        for i in s:
            if i is '(':
                stack.append('(')
                t=t+1
            elif i is ')':
                stack.pop()
                t=t-1
            
            if t>mx:
                mx=t
        return mx
