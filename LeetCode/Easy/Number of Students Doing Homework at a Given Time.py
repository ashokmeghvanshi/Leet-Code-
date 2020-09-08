class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        s=0
        for i, j in zip(startTime,endTime):
            if queryTime in range(i,j+1):
                s=s+1
        return s
