class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        elif len(cost) == 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost[0],cost[1])
        
        for i in range(len(cost)-3,-1,-1):
            cost[i] = min(cost[i]+cost[i+1],cost[i]+cost[i+2])
            
        
        return min(cost[0],cost[1])