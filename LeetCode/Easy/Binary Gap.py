class Solution:
    def binaryGap(self, n: int) -> int:
        
        s=bin(n)[2:]
        print(s)
        if s.count('1')<2:
            return 0
        
        mxd=0

        # Solution 1

        i=0
        while i<len(s)-1:
            if s[i]=='1':
                j=i+1
                while j<len(s):
                    if s[j]=='1':
                        if abs(j-i)>mxd:
                            mxd=abs(j-i)
                        break
                        
                            
                    j=j+1
            i=i+1
            #print(i,j,mxd)

        # Solution 2

        # l=[]
        # for i in range(len(s)):
        #     if s[i]=='1':
        #         l.append(i)
        
        # for i in range(len(l)-1):
        #     if abs(l[i+1]-l[i])>mxd:
        #         mxd=abs(l[i+1]-l[i])
        return mxd
        
                        
