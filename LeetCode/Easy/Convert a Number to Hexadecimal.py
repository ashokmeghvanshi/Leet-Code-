class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return '0'
        if num < 0:
            num = num + 2**32
        
        if num>0:
            res=''
            d={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
            while num>0:
                r=num%16
                if r<10:
                    res=res+str(r)
                else:
                    res=res+d[r]
                num=num//16
            
            return res[::-1]
