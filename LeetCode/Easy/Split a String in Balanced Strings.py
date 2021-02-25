class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        st=[]
        res=0
        t=0
        for i in s:
            if len(st)==0:
                st.append(i)
            else:
                if i=='L' and st[-1]=='R':
                    t=t+1
                    st=st[:-1]
                elif i=='R' and st[-1]=='L':
                    t=t+1
                    st=st[:-1]
                elif i=='L' and st[-1]=='L':
                    st.append(i)
                elif i=='R' and st[-1]=='R':
                    st.append(i)
                    
            if len(st)==0:
                res=res+1
        return res
                    
            
