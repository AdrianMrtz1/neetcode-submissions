class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_max(nums):
            prev1 = 0
            prev2 = 0
            for i in nums:
                current = max(prev1, i+prev2)
                prev2 = prev1
                prev1 = current
            return prev1
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            return max(rob_max(nums[0:n-1]), rob_max(nums[1:n]))
                