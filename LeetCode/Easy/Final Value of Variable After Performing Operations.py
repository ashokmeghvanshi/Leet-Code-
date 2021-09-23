class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        plus=0
        minus=0
        
        for i in operations:
            if '+' in i:
                plus=plus+1
            
            if '-' in i:
                minus=minus+1
        
        return plus-minus
