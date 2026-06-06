"""Given a string s, find the length of the longest substring without duplicate characters."""

# Solution:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen    = {}  # char → last seen index
        left    = 0
        max_len = 0

        for right, char in enumerate(s):

            if char in seen and seen[char] >= left:
                left = seen[char] + 1  # shrink window

            seen[char] = right                        # update index
            max_len = max(max_len, right - left + 1)  # update answer

        return max_len