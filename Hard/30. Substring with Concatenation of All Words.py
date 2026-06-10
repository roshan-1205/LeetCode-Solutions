"""You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order."""

from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        w_len = len(words[0])
        w_count = len(words)
        total = w_len * w_count
        word_freq = Counter(words)
        result = []

        for offset in range(w_len):
            left = offset
            cur = Counter()
            matched = 0

            for right in range(offset, len(s) - w_len + 1, w_len):
                word = s[right:right + w_len]
                if word in word_freq:
                    cur[word] += 1
                    matched += 1
                    while cur[word] > word_freq[word]:
                        left_word = s[left:left + w_len]
                        cur[left_word] -= 1
                        matched -= 1
                        left += w_len
                    if matched == w_count:
                        result.append(left)
                        left_word = s[left:left + w_len]
                        cur[left_word] -= 1
                        matched -= 1
                        left += w_len
                else:
                    cur.clear()
                    matched = 0
                    left = right + w_len

        return result