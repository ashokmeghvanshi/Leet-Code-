class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        stack=[]
        t=''
        res=[]
        for i in S:
            if i is '(':
                stack.append(i)
                t=t+i
            else:
                if stack.pop()=='(':
                    t=t+i
                if len(stack)<1:
                    res.append(t)
                    t=''
        fres=''
        for i in res:
            if len(i)>2:
                fres=fres+i[1:-1]
        return fres
            
