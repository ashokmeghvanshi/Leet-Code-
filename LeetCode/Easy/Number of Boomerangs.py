class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        s=0
        for i in points:
            d={}
            for j in points:
                dis=(((i[0]-j[0])**2)+((i[1]-j[1])**2))**0.5
                if dis in d:
                    d[dis]=d[dis]+1
                else:
                    d[dis]=1
            #print(d)
            for k in d:
                s=s+(d[k]*(d[k]-1))
        return s
