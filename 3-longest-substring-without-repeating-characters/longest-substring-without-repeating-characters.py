class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        maxl = float('-inf')
        seen = set()

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left+=1
                
            
            seen.add(s[right])
            maxl = max(maxl, right - left +1)

        return 0 if maxl == float('-inf') else  maxl
        