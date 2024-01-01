class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        totalWater = 0
        
        MaxLeft = height[0]
        MaxRight = height[right]
        MaxHeightIndex = height.index(max(height))
        
        while(left < MaxHeightIndex):
            if (MaxLeft < height[left]):
                MaxLeft = height[left]
            else :
                totalWater += MaxLeft - height[left] # Add difference of height
            left += 1
        
        while(right > MaxHeightIndex):
            if (MaxRight < height[right]):
                MaxRight = height[right]
            else :
                totalWater += MaxRight - height[right]
            right -= 1
        
        return totalWater
