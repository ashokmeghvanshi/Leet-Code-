class OrderedStream:

    def __init__(self, n: int):
        self.d=['']*n
        self.ptr=0
        
    def insert(self, id: int, value: str) -> List[str]:
        self.d[id-1]=value
        
        res=[]
        
        for i in range(self.ptr,len(self.d)):
            if self.d[i]=='':
                break
            else:
                res.append(self.d[i])
                self.ptr=i+1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
