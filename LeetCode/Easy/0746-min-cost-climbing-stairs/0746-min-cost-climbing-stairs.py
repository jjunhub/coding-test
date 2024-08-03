class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        answer = [0] * n
        # index 0 for one step, 1 for two step
        answer[0] = cost[0]
        answer[1] = cost[1]
        
        for i in range(2, n):
            answer[i] = min(answer[i-1] + cost[i], answer[i-2] + cost[i])
        
        return min(answer[n-1], answer[n-2])
    