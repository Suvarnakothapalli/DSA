class Solution(object):
    def moveZeroes(self, nums):
        count = nums.count(0)
        for i in range(count):
            nums.remove(0)
        for i in range(count):
            nums.append(0)
       
        