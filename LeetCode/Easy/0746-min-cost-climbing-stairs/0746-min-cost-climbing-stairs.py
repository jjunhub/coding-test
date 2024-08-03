class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        
        answer = [[0, 0] for _ in range(n)]
        # index 0 for one step, 1 for two step
        answer[0][0] = cost[0]
        answer[0][1] = cost[0]
        answer[1][0] = min(answer[0]) + cost[1]
        answer[1][1] = cost[1]
        
        for i in range(2, n):
            answer[i][0] = min(answer[i-1]) + cost[i]
            answer[i][1] = min(answer[i-2]) + cost[i]
        
        return min(min(answer[n-2]), min(answer[n-1]))
    