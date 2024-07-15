class Solution:
    def minFlips(self, target: str) -> int:
        count = 0
        prevchar = '0'
        
        for i in target:
            if i != prevchar:
                count+=1
                prevchar = i
        return count 


