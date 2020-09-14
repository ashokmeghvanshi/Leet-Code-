class Solution:
    def findComplement(self, num: int) -> int:
        num=bin(num)[2:]
        s=''
        for i in num:
            if i=='0':
                s=s+'1'
            else:
                s=s+'0'
        return int(s,2)
