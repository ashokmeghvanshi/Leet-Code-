class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a=['q','w','e','r','t','y','u','i','o','p']
        b=['a','s','d','f','g','h','j','k','l']
        c=['z','x','c','v','b','n','m']
        result=[]
        for i in words:
            h,m,l=0,0,0
            for j in i.lower():
                if j in a:
                    h=h+1
                if j in b:
                    m=m+1
                if j in c:
                    l=l+1
                else:
                    pass
            if h==len(i) or m==len(i) or l==len(i):
                result.append(i)
                
        return result
