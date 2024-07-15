class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        icecream = 0
        for i in range(len(costs)):
            if costs[i]<=coins:
                coins=coins-costs[i]
                icecream +=1
            else:
                break
        return icecream