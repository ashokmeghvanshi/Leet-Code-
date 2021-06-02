class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        def check(index,rule):
            ans=0
            for i in items:
                if i[index]==rule:
                    ans=ans+1
            return ans
            
        if ruleKey=='type':
            return check(0,ruleValue)
        if ruleKey=='color':
            return check(1,ruleValue)
        if ruleKey=='name':
            return check(2,ruleValue)
