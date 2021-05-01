class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        d={5:0,10:0}
        y=0
        for i in bills:
            if i==5:
                d[i]=d[i]+1
                
            elif i==10:
                if d[5]>=1:
                    d[5]=d[5]-1
                    d[i]=d[i]+1
                else:
                    #print('A',d,bills.index(i),i)
                    return False
                
            elif i==20:
                if d[5]>=1 and d[10]>=1:
                    d[5]=d[5]-1
                    d[10]=d[10]-1
                    
                elif d[5]>=3:
                    d[5]=d[5]-3

                else:
                    #print('W',d,y,i)
                    return False
            y=y+1
            #print(d,i,y)
        return True
        
        
        
        
        
