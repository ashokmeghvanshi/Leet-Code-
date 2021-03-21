class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        result=releaseTimes[0]
        key=[keysPressed[0]]
        num=[releaseTimes[0]]
        
        for i in range(1,len(releaseTimes)):
            t=releaseTimes[i]-result
            result=releaseTimes[i]
            if num[-1]<t:
                num[-1]=t
                key[-1]=keysPressed[i]
            elif num[-1]==t:
                num.append(t)
                if key[-1]<keysPressed[i]:
                    key[-1]=keysPressed[i]
                else:
                    pass
        #print(num,key)
        return key[0]
            
                
            
