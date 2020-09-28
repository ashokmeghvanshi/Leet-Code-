class Solution:
    def isUgly(self, num: int) -> bool:
        if num==0 or num<0:
            return False
        t=[]
        while num%2==0:
            num=num//2
            if 2 not in t:
                t.append(2)
        
        while num%3==0:
            num=num//3
            if 3 not in t:
                t.append(3)
                
        while num%5==0:
            num=num//5
            if 5 not in t:
                t.append(5)
        if num==1:
            return True
        else:
            return False
