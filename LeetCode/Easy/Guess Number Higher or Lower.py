# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low=1
        high=n
        while low<=high:
            val=(low+high)//2
            if guess(val)==0:
                return val
            elif guess(val)==1:
                low=val+1
            else:
                high=val-1
            
                
            
