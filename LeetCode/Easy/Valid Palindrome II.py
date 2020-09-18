class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        else:
            p= s[::-1]
            for i in range(len(s)):
                if s[i]!=p[i]:
                    t=s[:i]+s[i+1:]
                    w=p[:i]+p[i+1:]
                    if t==t[::-1]:
                        return True
                    if w==w[::-1]:
                        return True
                    else:
                        return False

            return False
