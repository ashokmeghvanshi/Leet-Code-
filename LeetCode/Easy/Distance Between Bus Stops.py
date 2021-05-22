class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        a,p=0,0
        ind=[x for x in range(len(distance))]
        #print(ind)
        t=ind+ind[:-1]
        #print(t)
        if start>destination:
            start,destination=destination,start
        #print(start,destination)
        i=start
        while i<len(t):
            if t[i]==destination:
                break
            else:
                a=a+distance[t[i]]
            i=i+1
            
        i=destination
        while i<len(t):
            #print(t[i],distance[t[i]])
            if t[i]==start:
                break
            else:
                p=p+distance[t[i]]
            i=i+1
        #print(a,p)
        return min(a,p)
