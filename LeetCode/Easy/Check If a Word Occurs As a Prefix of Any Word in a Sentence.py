class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split()
        for i in range(len(sentence)):
            #print(sentence[i])
            t=len(searchWord)
            if searchWord in sentence[i][:t]:
                return i+1
        return -1
