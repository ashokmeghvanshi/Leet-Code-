class Solution:
    def isPathCrossing(self, path: str) -> bool:    
        d=[[0,0]]
        start_pos=[0,0]
        for i in path:
            if i=='N':
                start_pos=[d[-1][0],d[-1][1]+1]
            if i=='S':
                start_pos=[d[-1][0],d[-1][1]-1]
            if i=='E':
                start_pos=[d[-1][0]+1,d[-1][1]]
            if i=='W':
                start_pos=[d[-1][0]-1,d[-1][1]]
            #print(d,start_pos)
            if start_pos in d:
                return True
            d.append(start_pos)
        return False
