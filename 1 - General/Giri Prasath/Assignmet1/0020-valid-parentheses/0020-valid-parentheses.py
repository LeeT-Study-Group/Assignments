class Solution:
    def isValid(self, s: str) -> bool:
            if len(s) % 2 != 0:
                return False
            paren = {"(": ")", "[": "]", "{": "}"}
            stk = []  

            for i in s:
                if i in paren:
                    stk.append(i)  
                elif stk and i == paren[stk[-1]]:
                    stk.pop()  
                else:
                    return False  

            return len(stk) == 0  
                        