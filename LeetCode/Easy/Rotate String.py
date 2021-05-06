class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        
        
        if A=='' and B=='':
            return True
        
        if A=='' or B=='':
            return False
        
        check=A
        while True:
            if A==B:
                return True
            else:
                A=A[1:]+A[0]
            if A==check:
                break
        return False
