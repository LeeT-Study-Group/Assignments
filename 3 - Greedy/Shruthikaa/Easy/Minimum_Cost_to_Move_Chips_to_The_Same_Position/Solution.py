class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evencount = 0
        oddcount= 0

        for i in position:
            if i%2==0:
                evencount+=1
            else:
                oddcount +=1
        return min(evencount,oddcount)