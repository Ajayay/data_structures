class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==0:
            return 1
        elif len(cost) == 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost)
        else:
            
        
            new_list = []
            new_list_size = len(cost)+1

            for i in cost:
                new_list.append(i)

            new_list.append(0)

            # print(new_list)
            for i in range(new_list_size-3, -1,-1):

                new_list[i] = min(new_list[i]+new_list[i+1],new_list[i]+new_list[i+2] )

        
        return min(new_list[0],new_list[1])
                