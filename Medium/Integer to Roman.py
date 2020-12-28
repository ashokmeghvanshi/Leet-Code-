class Solution:
    def intToRoman(self, num: int) -> str:
        
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        roman = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        rs=''
        i=0
        while num>0:
            for _ in range(num//val[i]):
                rs=rs+roman[i]
                num=num-val[i]
            i=i+1
        return rs
