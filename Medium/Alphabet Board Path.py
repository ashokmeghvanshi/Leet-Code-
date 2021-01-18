class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board=[["a","b","c","d","e"],
               ["f","g","h","i","j"],
               ["k","l","m","n","o"],
               [ "p","q","r","s","t"],
               ["u","v","w","x","y"],
               ["z"]]
        
        cx,cy=0,0
        res=''
        t=0
        for i in target:
            for j in range(len(board)):
                if i in board[j]:
                    #print(board[j].index(i),j,res,i)
                    
                    if j==cy and board[j].index(i)==cx:
                        res=res+'!'
                        break
                    if cy<j:
                        if (cx!=0 or cy!=0) and j>4:
                            t=t+1
                            res=res+'D'*abs(j-cy-1)
                        else:
                            res=res+'D'*abs(j-cy)

                    if cy>j:
                        res=res+'U'*abs(j-cy)
                        
                    if cx<board[j].index(i):
                        res=res+'R'*abs(board[j].index(i)-cx)
                    
                    if cx>board[j].index(i):
                        res=res+'L'*abs(board[j].index(i)-cx)
                        
                    cy,cx=j,board[j].index(i)
                    #print('t',t)
                    if t==0:
                        res=res+'!'
                    if t==1:
                        res=res+'D!'
                        t=0
        return res
        
