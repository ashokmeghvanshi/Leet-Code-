class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        stack=[]
        for i in ops:
            if not stack or ( i!='+' and i!='D' and i!='C'):
                stack.append(int(i))
            else:
                if i=='+':
                    t=stack[-1]+stack[-2]
                    stack.append(t)
                elif i=='D':
                    t=stack[-1]*2
                    stack.append(t)
                if i=='C':
                    stack.pop()
        return sum(stack)
                
            
