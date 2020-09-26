class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        seq=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-"                  ,"-.--","--.."]
        d=[]
        for i in words:
            s=''
            for j in i:
                s=s+seq[ord(j)-97]
            d.append(s)
        p=list(dict.fromkeys(d))
        return len(p)
