class Solution:
    def average(self, salary: List[int]) -> float:
        
        s=sorted(salary)
        p=sum(s[1:-1])/(len(s)-2)
        return p
