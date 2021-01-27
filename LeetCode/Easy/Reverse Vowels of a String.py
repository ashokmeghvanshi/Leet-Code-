class Solution:
    def reverseVowels(self, s: str) -> str:
        t=[]
        for i in s:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                t.append(i)
        t=t[::-1]
        a=''
        j=0
        for i in s:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                a=a+t[j]
                j=j+1
            else:
                a=a+i
        return a
        
