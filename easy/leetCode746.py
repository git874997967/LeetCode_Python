#746. Min Cost Climbing Stairs
def minCostClimbingStairs(cost):
    if len(cost) == 1:
        return cost[0]
    
    for i in range(2,len(cost)  ):
        cost[i] = min(cost[i] + cost[i-1] , cost[i]+cost[i-2])

    return min(cost[-1],cost[-2])


print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))


print(minCostClimbingStairs([10,14,20]))