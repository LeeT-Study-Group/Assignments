class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openc = 0
        close = 0
        for i in s:
            if i=="(":
                openc +=1
            elif i == ")":
                if openc > 0:
                    openc -= 1
                else:
                    close +=1
        
        return close+openc