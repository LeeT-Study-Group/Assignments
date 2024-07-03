class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        warm_wait = [0]*len(temperatures)
        for ind, temp in enumerate(temperatures):
            while stk and stk[-1][1] < temp:
                day = stk.pop()
                warm_wait[day[0]] = ind - day[0]
            stk.append((ind,temp))
        return warm_wait