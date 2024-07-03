class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        hash_table = {}
        max_len = 0

        for i in range(len(s)):
            if s[i] in hash_table and hash_table[s[i]] >= start:
                while s[start] != s[i]:
                    start += 1
                start += 1

            hash_table[s[i]] = i
            if max_len < i-start+1:
                max_len = i-start+1

        return max_len
        