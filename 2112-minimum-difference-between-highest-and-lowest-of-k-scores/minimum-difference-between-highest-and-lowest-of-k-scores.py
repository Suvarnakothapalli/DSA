class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()

        left = 0
        right = 0
        minDiff = float('inf')

        while right < len(nums):
            
            if right - left + 1 == k:
                diff = nums[right] - nums[left]
                minDiff = min(minDiff, diff)
                left += 1

            right += 1

        return minDiff
        