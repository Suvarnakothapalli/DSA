class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        left = 0
        minDiff = float('inf')
        for right in range(0,len(nums)):
            if right - left + 1 == k:
                diff = nums[right] - nums[left]
                minDiff = min(minDiff,diff)
                left +=1 
        return minDiff

       
        