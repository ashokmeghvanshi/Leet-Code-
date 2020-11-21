class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a=[]
        b=[]
        for i in S:
            if not a and i!='#':
                a.append(i)
            elif not a and i=='#':
                pass
            elif a and i=='#':
                a.pop()
            else:
                a.append(i)
        a=''.join(a)
        print(a)
        for i in T:
            if not b and i!='#':
                b.append(i)
            elif not b and i=='#':
                pass
            elif b and i=='#':
                b.pop()
            else:
                b.append(i)
        b=''.join(b)

        #print(b)
        if a==b:
            return True
        return False
            
                
