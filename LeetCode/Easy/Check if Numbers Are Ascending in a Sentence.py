class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        s=s.split(' ')
        #print(s)
        
        nums=[]
        for i in s:
            if i.isdigit():
                if len(nums)==0:
                    nums.append(int(i))
                else:
                    if nums[-1]<int(i):
                        nums.append(int(i))
                    else:
                        return False
        return True
