class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minNum = 0
        maxNum = 0
        bestNum = 0
        for i in range(len(nums)):
            num = nums[i]
            if i == 0:
                minNum, maxNum, bestNum = nums[i],nums[i],nums[i]
                continue
            minNum, maxNum = min(minNum * num, maxNum * num, num), max(minNum * num, maxNum * num, num)
            if maxNum > bestNum:
                bestNum = maxNum
        return bestNum
   