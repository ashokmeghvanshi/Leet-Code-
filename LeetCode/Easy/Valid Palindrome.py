class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=''
        for i in s:
            if i.isalnum():
                t=t+i.lower()
        if t==t[::-1]:
            return True
        else:
            return False
