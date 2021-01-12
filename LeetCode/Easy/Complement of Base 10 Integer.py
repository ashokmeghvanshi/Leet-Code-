class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        s=bin(N)[2:]
        s=list(s)
        for i in range(len(s)):
            if s[i]=='1':
                s[i]='0'
            else:
                s[i]='1'
        new_num=''.join(s)
        new_num=int(new_num,2)
        return  new_num
