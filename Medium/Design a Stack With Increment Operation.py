Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.maxSize=maxSize
        self.MXS=0
        
    def push(self, x: int) -> None:
        if self.MXS<self.maxSize:
            self.stack.append(x)
            self.MXS=self.MXS+1
    def pop(self) -> int:
        if len(self.stack)==0:
            return -1
        else:
            self.MXS=self.MXS-1
            return self.stack.pop()
            
    def increment(self, k: int, val: int) -> None:
        
        if len(self.stack)<k:
            for i in range(len(self.stack)):
                self.stack[i]=self.stack[i]+val
        else:
            for i in range(k):
                self.stack[i]=self.stack[i]+val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)