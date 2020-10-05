class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        t=[0]*num_people
        s=1
        i=0
        while candies>0:
            #print(t,candies,s,i)
            if candies<s:
                t[i]=t[i]+candies
                break
            t[i]=t[i]+s
            if i==num_people-1:
                i=0
            else:
                i=i+1
            candies=candies-s
            s=s+1
        #print(t,candies,s,i)
        return t
            
        
