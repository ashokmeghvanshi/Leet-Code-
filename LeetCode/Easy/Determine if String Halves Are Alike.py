class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        half=len(s)//2
        x,y=0,0
        for i in range(len(s)):
            if s[i] in vowels:
                if i<half:
                    x=x+1
                if i>=half:
                    y=y+1

        if x==y:
            return True
        return False
