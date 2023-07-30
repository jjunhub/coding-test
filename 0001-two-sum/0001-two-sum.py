class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        results = []
        while (True):
            hap = new_nums[i] + new_nums[j]
            if(hap == target):
                if(nums.index(new_nums[i]) == nums.index(new_nums[j])) :
                    results.append(nums.index(new_nums[i]))
                    nums.remove(new_nums[i])
                    results.append(nums.index(new_nums[j]) + 1)
                else :
                    results.append(nums.index(new_nums[i]))
                    results.append(nums.index(new_nums[j]))
                return results
            elif(hap > target) :
                j -= 1
            else :
                i += 1