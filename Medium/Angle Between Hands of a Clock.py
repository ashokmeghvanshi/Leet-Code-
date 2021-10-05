class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a=abs((60*hour - 11*minutes)/2)
        b=360-a
        return min(a,b)
