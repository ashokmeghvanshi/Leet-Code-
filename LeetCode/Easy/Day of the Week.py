class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
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
        
        y=year
        m=month
        d=day
        l=[]
        if checkYear(y)==True:
            l=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            l=[31,28,31,30,31,30,31,31,30,31,30,31]
        no_day=0
        no_day=no_day+sum(l[:m-1])
        no_day=no_day+d
        
        #count for all years
        for i in range(1971,y):
            if checkYear(i)==True:
                no_day=no_day+366
            else:
                no_day=no_day+365
        #print(no_day,no_day%7)
        dayname=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        return dayname[no_day%7-4]
        
