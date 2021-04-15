class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        m = {}
        
        for cp in cpdomains:
            split = cp.split(" ")
            n,t=int(split[0]), split[1]
            j=0
            if t not in m:
                m[t]=n
            else:
                m[t]+=n
                
            while j<len(t):
                if t[j]=='.':
                    if t[j+1:] not in m:
                        m[t[j+1:]]=n
                    else:
                        m[t[j+1:]]+=n
                j=j+1
        
        # now iterate hashmap and get each
        return [str(m[key]) + " " + key for key in m]
    
        # m={}
        # for i in cpdomains:
        #     no,d=i.split(" ")
        #     no=int(no)
        #     l=d.split(".")
        #     print(l)
        #     for i in range(len(l)):
        #         k='.'.join(l[i:])
        #         print(k)
        #         if k not in m:
        #             m[k]=no
        #         else:
        #             m[k]+=no
        # print(m)
        # m = sorted(m.items(), key=lambda kv: kv[1])
        # #print(mapping)
        # ans=[]
        # for i,no in m:
        #     ans.append(str(no)+" "+str(i))
        # # print(ans)
        # return ans
