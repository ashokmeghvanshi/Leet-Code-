class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack=[homepage]
        self.st=0
    
    def visit(self, url: str) -> None:
        
        #self.stack.append(url)
        
        self.stack=self.stack[:self.st+1]+[url]
        self.st+=1
        #print(self.stack,self.st)

    def back(self, steps: int) -> str:
        if len(self.stack)>0:
            
            self.st=max(self.st-steps,0)
            #print('1',self.stack,self.st)
            #self.stack.append(self.stack[self.st])
            return self.stack[self.st] 

    def forward(self, steps: int) -> str:
        if len(self.stack)>0:
            self.st=min(steps+self.st,len(self.stack)-1)
            #print('2',self.stack,self.st)
            #self.stack.append(self.stack[self.st])
            return self.stack[self.st] 

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
