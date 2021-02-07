class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        
        for i in s:
            if not stack or i!=stack[-1]:
                stack.append(i)
            elif stack and i==stack[-1]:
                stack.pop()
            #print(stack)
        return ''.join(stack)
                
            
            
            
            
            
        
        
