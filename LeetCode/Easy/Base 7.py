class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return str(num)
        sign=''
        if num<0:
            sign='-'
        num=abs(num)
        result=[]
        
        while num>0:
            result.append(str(num%7))
            num=num//7
            
        result.append(sign)
        return ''.join(result[::-1])
