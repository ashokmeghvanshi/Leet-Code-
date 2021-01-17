class Solution:
    def findRestaurant(self, l1: List[str], l2: List[str]) -> List[str]:
        key=[]
        val=[]
        if len(l1)<len(l2):
            for i in l1:
                if i in l2:
                    key.append(i)
                    val.append(l1.index(i)+l2.index(i))            
        else:
            for i in l2:
                if i in l1:
                    key.append(i)
                    val.append(l1.index(i)+l2.index(i))
        
        if len(key)==1:
            return key
        else:
            p=[]
            for i in range(len(val)):
                if val[i]==min(val):
                    p.append(key[i])
            return p
