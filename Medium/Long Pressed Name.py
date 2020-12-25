class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        a,b = 0,0
        stack = []
        while b<len(typed):
            if a<len(name) and name[a]== typed[b]:
                a +=1
            elif a==0 or name[a-1]!=typed[b]:
                return False
            b=b+1
        return a == len(name)
