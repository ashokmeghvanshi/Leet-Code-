class Solution:
    def freqAlphabets(self, s: str) -> str:
        t=''
        p=['1','2','3','4','5','6','7','8','9']
        d={'1':'a','2':'b',
           '3':'c','4':'d',
           '5':'e','6':'f',
           '7':'g','8':'h',
           '9':'i','10#':'j',
           '11#':'k','12#':'l',
           '13#':'m','14#':'n',
           '15#':'o','16#':'p',
           '17#':'q','18#':'r',
           '19#':'s','20#':'t',
           '21#':'u','22#':'v',
           '23#':'w','24#':'x',
           '25#':'y','26#':'z'}
        i=0
        while i<len(s)-2:
            
            if s[i+2]!='#':
                t=t+d[s[i:i+1]]
                i=i+1
                
            elif s[i+2]=='#' and s[i+1]!='#' and s[i] in p and s[i:i+3] in d:
                t=t+d[s[i:i+3]]
                i=i+3
                
        while i<len(s):
            t=t+d[s[i:i+1]]
            i=i+1
            
        return t
