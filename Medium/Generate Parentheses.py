class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def GP(res,s,n,openp,closep):
            if len(s)==2*n:
                res.append(s)
            if openp<n:
                GP(res,s+'(',n,openp+1,closep)
            if openp>closep:
                GP(res,s+')',n,openp,closep+1)
                
        res=[]
        s=''
        openp,closep=0,0
        GP(res,s,n,openp,closep)
        return res
    
