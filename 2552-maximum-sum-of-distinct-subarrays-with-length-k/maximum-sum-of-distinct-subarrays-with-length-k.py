class Solution(object):
    def maximumSubarraySum(self, nums, k):
        currS = 0
        maxS = 0
        left = 0
        seen = set()

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                currS -= nums[left]
                left += 1

            currS += nums[right]
            seen.add(nums[right])

            if right - left + 1 == k:
                maxS = max(currS, maxS)
                currS -= nums[left]
                seen.remove(nums[left])
                left += 1

        return maxS
        
        