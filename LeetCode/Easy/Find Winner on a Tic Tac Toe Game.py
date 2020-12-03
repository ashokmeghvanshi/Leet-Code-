class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        def decidewins(s,tt):
            if tt[0][0]==s and tt[0][1]==s and tt[0][2]==s: 
                return True
            if tt[1][0]==s and tt[1][1]==s and tt[1][2]==s: 
                return True
            if tt[2][0]==s and tt[2][1]==s and tt[2][2]==s: 
                return True
            if tt[0][0]==s and tt[1][0]==s and tt[2][0]==s: 
                return True
            if tt[0][1]==s and tt[1][1]==s and tt[2][1]==s: 
                return True
            if tt[0][2]==s and tt[1][2]==s and tt[2][2]==s: 
                return True
            if tt[0][0]==s and tt[1][1]==s and tt[2][2]==s: 
                return True
            if tt[0][2]==s and tt[1][1]==s and tt[2][0]==s: 
                return True
            return False
        
        tt=[["   " for i in range(3)]for j in range(3)]
        chance='A'
        turn=1
        for k in moves:
            i,j = k[0],k[1]
            if turn%2==0:
                tt[i][j] = 'O'
            else:
                tt[i][j] = 'X'
            turn=turn+1
        if decidewins('X',tt):
            return 'A'
        elif decidewins('O',tt):
            return 'B'
        if len(moves)==9:
            return 'Draw'
        else:
            return 'Pending'
