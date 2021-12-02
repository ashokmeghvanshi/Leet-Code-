class Solution:
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        
        def LogSort(Log):
            Log= Log.split(' ')
            #print([Log[1:], Log[0]])
            return [Log[1:], Log[0]]
        
        alpha=[]
        digit=[]
        
        for i in logs:
        
            t=i.split()
            if t[1].isdigit()==True:
                digit.append(i)
                
            else:
                alpha.append(i)
        
        
        alpha.sort(key =lambda x:x.split()[0])
        
        alpha.sort(key=lambda x:x.split()[1:])
        
        #alpha=sorted(alpha, key=LogSort)
        
        return alpha+digit
