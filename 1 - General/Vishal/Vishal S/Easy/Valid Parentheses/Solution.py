class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for x in s:
            if x in ["(", "{", "["]:
                stk.append(x)
            else:
                if stk and ( (x == ")" and stk[-1] == "(") or (x=="}" and stk[-1] == "{") or (x=="]" and stk[-1]=="[")):
                    stk.pop()
                else:
                    return False

        return len(stk) == 0