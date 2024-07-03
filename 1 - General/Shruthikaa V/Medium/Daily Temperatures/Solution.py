class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        templen = len(temperatures)
        result = [0] * templen
        stack = []
        
        for i in range(templen):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        
        return result
