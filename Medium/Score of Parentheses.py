class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        
        score=0
        stack=[]
        for i in S:
            if (not stack and i=='(' ) or (i=='(' ):
                stack.append(i)
            else:
                d=stack.pop()
                if d=='(':
                    stack.append(1)
                else:
                    score=0
                    while d!='(':
                        score=score+d
                        d=stack.pop()
                    stack.append(2*score)
        #print(stack)
        return sum(stack)
