class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        s=''
        for i in range(len(word)):
            if word[i] in ['0','1','2','3','4','5','6','7','8','9']:
                s=s+word[i]
        ans=[]
        i=0
        check=''
        for j in range(len(word)):
            if word[j] in ['0','1','2','3','4','5','6','7','8','9']:
                if word[j]==s[i]:
                    check=check+s[i]
                    i=i+1
            else:
                #print(check)
                if check!='' and int(check) not in ans:
                    ans.append(int(check))
                check=''
        #print(check)
        if check!='' and int(check) not in ans:
            ans.append(int(check))
        return len(ans)
        
