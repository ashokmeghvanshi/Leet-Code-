class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            f=''
            if stack:
                f=stack[-1]
            if stack and i==f.upper() and i!=f:
                stack.pop()
            elif stack and i.upper()==f and i!=f:
                stack.pop()
            elif not stack or i!=f.upper() or i.upper()!=f or i==f:
                stack.append(i)
            #print(stack)
        return ''.join(stack)
                
