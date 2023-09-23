class Solution:
    def climbStairs(self, n: int) -> int:
        a = [0] * 48
        a[1] = 1
        a[2] = 1
        for i in range(1, n+1):
            a[i+1] += a[i]
            a[i+2] += a[i]
    
        return a[n]
            
        