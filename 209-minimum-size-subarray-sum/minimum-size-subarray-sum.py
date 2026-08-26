class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        totalS= 0
        min_len = float('inf')

        for right in range(len(nums)):
            totalS += nums[right]

            while totalS >= target:
                min_len = min(min_len, right - left + 1)
                totalS -= nums[left]
                left += 1

        if min_len == float('inf'):
            return 0

        return min_len