class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack=[]
        
        for i in S:
            if not stack:
                stack.append(i)
            else:
                if stack[-1]=='(' and i==')':
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)
