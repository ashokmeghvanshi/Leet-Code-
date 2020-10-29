class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=''
        for i in address:
            if i=='.':
                s=s+'[.]'
            else:
                s=s+i
        #return address.replace('.','[.]')
        return s
