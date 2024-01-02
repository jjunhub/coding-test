class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMul = [1]
        rightMul = [1]
        result = []
        totalLeftMul = 1
        totalRightMul = 1
        
        for i in range(len(nums)-1):
            totalLeftMul *= nums[i]
            leftMul.append(totalLeftMul)
            
        for i in range(len(nums) - 1, 0, -1):
            totalRightMul *= nums[i]
            rightMul.append(totalRightMul)
            
        for i in range(len(nums)):
            result.append(leftMul[i] * rightMul[len(nums) -1 -i])
        return result
            