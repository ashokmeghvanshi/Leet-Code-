class Solution:
    def reformatDate(self, date: str) -> str:
        d=date.split()
        day=''
        for i in d[0]:
            if i in ['0','1','2','3','4','5','6','7','8','9']:
                day=day+i
        
        if int(day)<10:
            day='0'+day
            
        month=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        mi=month.index(d[1])+1
        m=''
        if mi<10:
            m='0'+str(mi)
        elif mi>9 and mi<13:
            m=str(mi)
                
        s=d[2]+'-'+m+'-'+day
        return s
