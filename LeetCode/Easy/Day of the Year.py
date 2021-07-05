class Solution:
    def dayOfYear(self, date: str) -> int:
        
        def checkYear(year):
            if (year % 4) == 0:
                if (year % 100) == 0:
                    if (year % 400) == 0:
                        return True
                    else:
                        return False
                else:
                     return True
            else:
                return False
            
        y=int(date[:4])
        m=int(date[5:7])
        d=int(date[8:])
        #print(y,m,d)
        #print(checkYear(y))
        l=[]
        if checkYear(y)==True:
            l=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            l=[31,28,31,30,31,30,31,31,30,31,30,31]
        #print(l)
        no_day=0
        for i in range(m-1):
            no_day=no_day+l[i]
        no_day=no_day+d
        return no_day
        
