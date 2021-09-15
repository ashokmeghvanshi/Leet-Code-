"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id1: int) -> int:
        
        def check(a,b,id1,employee):
            for i in a:
                for k in employees:
                    if k.id==i:
                        b=b+k.importance
                        if len(k.subordinates)>0:
                            b=b+check(k.subordinates,0,id1,employees)
            return b
        
        total=0
        for i in employees:
            if i.id==id1:
                total=total+i.importance
                if len(i.subordinates)>0:
                    total=total+check(i.subordinates,0,id1,employees)
               
        return total
