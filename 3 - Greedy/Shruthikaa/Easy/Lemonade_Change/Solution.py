class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changefive = 0
        changeten = 0
        for i in range(len(bills)):
            if bills[i]==5:
                changefive +=1
            elif bills[i]==10:
                if changefive >0:
                    changefive -=1
                    changeten +=1
                else:
                    return False
            else:
                if changeten > 0 and changefive > 0:
                    changeten -= 1
                    changefive -= 1
                elif changefive >= 3:
                    changefive -= 3
                else:
                    return False
        
        return True
                

        