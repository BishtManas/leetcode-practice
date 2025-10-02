class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empties = numBottles
        cost = numExchange

        while empties >= cost:
            empties -= cost    
            drunk += 1      
            empties += 1         
            cost += 1           

        return drunk
