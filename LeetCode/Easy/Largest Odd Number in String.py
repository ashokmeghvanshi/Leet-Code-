class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        i=len(num)-1
        while i>-1:
            if int(num[i])%2!=0:
                return num[:i+1]
            i=i-1
        return ''
        
        
#         # This solution is giving TLE
#         if int(num)%2!=0:
#             return num
        
#         def check(s):
#             if int(s)%2!=0:
#                 return True
#             return False
        
#         ans=0
#         for i in range(len(num)):
#             for j in range(i,len(num)):
#                 if check(num[i:j+1])==True:
#                     if int(num[i:j+1])>ans:
#                         ans=int(num[i:j+1])
#         if ans==0:
#             return ''
#         return str(ans)
