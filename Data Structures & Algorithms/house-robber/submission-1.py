class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        for i in nums:
            current = max(prev1, i+prev2)
            prev2 = prev1
            prev1 = current
        return prev1
            