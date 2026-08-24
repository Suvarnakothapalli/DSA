class Solution(object):
    def minimumRecolors(self, blocks, k):
        left = 0
        count = 0
        minimum = float('inf')

        for right in range(len(blocks)):
            
            if blocks[right] == 'W':
                count += 1
            if right - left + 1 == k:
                minimum = min(minimum, count)
                if blocks[left] == 'W':
                    count -= 1
                left += 1
        return minimum
        