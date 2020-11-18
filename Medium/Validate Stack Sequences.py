class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushi=0
        popi=0
        stack=[]
            
        if not pushed and not popped:
            return True
        elif pushed==popped:
            return True
        elif not pushed or not popped:
            return False
        else:
            while (pushi < len(pushed) and popi < len(popped)):
                stack.append(pushed[pushi])
                while stack and stack[-1]==popped[popi]:
                    stack.pop()
                    popi+=1
                
                pushi+=1
                    
            if stack:
                return False
            return True
