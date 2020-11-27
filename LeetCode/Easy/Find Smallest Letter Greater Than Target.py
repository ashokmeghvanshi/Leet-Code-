class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i>target:
                return i
        #print('s',letters[-1],target,letters[0])
        if letters[-1]<=target:
            return letters[0]
