"""Given an input string s and a pattern p, implement regular expression matching with support 
for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
Return a boolean indicating whether the matching covers the entire input string (not partial)."""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if p[j - 1] == '*':
                    zero_times = dp[i][j - 2]
                    one_plus   = dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.')
                    dp[i][j]   = zero_times or one_plus

                else:
                    char_match = p[j - 1] == s[i - 1] or p[j - 1] == '.'
                    dp[i][j]   = dp[i - 1][j - 1] and char_match

        return dp[m][n]