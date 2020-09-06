class Solution:
    def addDigits(self, num: int) -> int:
        if num<9:
            return num
        elif num%9==0:
            return 9
        else:
            return num%9
            
        ''''
        s=0
        while num>0:
            s=s+num%10
            num=num//10
            if num==0 and s>9:
                num=s
                s=0
        return s'''
