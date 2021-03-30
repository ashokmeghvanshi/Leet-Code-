class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        while True:
            if len(students)==0 or len(sandwiches)==0:
                return 0
            elif students[0]==sandwiches[0]:
                students=students[1:]
                sandwiches=sandwiches[1:]
            elif students[0]!=sandwiches[0]:
                if sandwiches[0] in students:
                    students=students[1:]+students[:1]
                else:
                    return len(students)
                
