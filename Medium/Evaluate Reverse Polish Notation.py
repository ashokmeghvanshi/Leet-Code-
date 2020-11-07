class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i not in ['+','-','*','/']:
                s.append(int(i))
            elif len(s)>1:
                if i=='/':
                    a=s.pop()
                    b=s.pop()
                    s.append(int(b/a))
                elif i=='-':
                    a=s.pop()
                    b=s.pop()
                    s.append(b-a)
                elif i=='+':
                    a=s.pop()
                    b=s.pop()
                    s.append(b+a)
                elif i=='*':
                    a=s.pop()
                    b=s.pop()
                    s.append(b*a)
        return s[0]
