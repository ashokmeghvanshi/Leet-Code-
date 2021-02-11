class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        a=1
        i=1
        while True:
            #print(digits,a)
            t=digits[-i]+a
            if t>9:
                a=t//10
                digits[-i]=t%10
                #print(digits,a,t,i)
                if a!=0 and i==len(digits):
                    digits.insert(0,a)
                    break
                
                #print('1',digits,a,t,i)
                
            else:
                digits[-i]=t
                break
            i=i+1
        return digits
        
        
