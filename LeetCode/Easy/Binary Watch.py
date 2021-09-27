class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        l1=[8,4,2,1]
        l2=[32,16,8,4,2,1]
        
        def sub_seq(arr,t):

            l1_sub=[]

            for i in range(sum(arr)-3):
                b=bin(i)[2:]
                if t>=b.count('1') or 0==b.count('1'):
                    l1_sub.append(b)
            return l1_sub
        
        p1=sub_seq(l1,turnedOn)
        p2=sub_seq(l2,turnedOn)
        #print(p1)
        #print(p2)
        ans=[]
        y=0
        for i in range(len(p1)):
            for j in range(len(p2)):
                c=p1[i]+p2[j]
                s=''
                if turnedOn==c.count('1'):
                    
                    y=y+1
                    n1=int(p1[i],2)
                    n2=int(p2[j],2)
                    if n1==0:
                        s=s+'0'
                    elif n1>0 and n1<10:
                        s=s+str(n1)
                    elif n1>9:
                        s=s+str(n1)
                        
                    s=s+':'
                    if n2==0:
                        s=s+'00'
                    elif n2>0 and n2<10:
                        s=s+'0'+str(n2)
                    elif n2>9:
                        s=s+str(n2)
                    #print(c,n1,n2,s)
                    
                    ans.append(s)
        #print(y)
        return ans
