class Solution:
    def maxNumberOfBalloons(self, test: str) -> int:
        l=[test.count('b'),test.count('a'),test.count('l')//2,test.count('o')//2,test.count('n')]
        return min(l)
