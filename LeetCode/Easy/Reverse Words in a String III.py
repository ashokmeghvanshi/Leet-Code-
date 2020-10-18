class Solution:
    def reverseWords(self, s: str) -> str:
        t=''
        for i in s.split():
            t=t+i[::-1]+' '
        t=t[:-1]
        return t
