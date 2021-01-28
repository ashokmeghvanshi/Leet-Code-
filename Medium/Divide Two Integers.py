class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if (dividend < 0) ^  (divisor < 0):
            sign = -1
        else:
            sign = 1
        dividend = abs(dividend) 
        divisor = abs(divisor) 

        quotient = 0
        temp=0
        for i in range(31, -1, -1): 
            if (temp + (divisor << i) <= dividend): 
                temp += divisor << i; 
                quotient |= 1 << i; 


        return min(sign * quotient,2**31-1) 
