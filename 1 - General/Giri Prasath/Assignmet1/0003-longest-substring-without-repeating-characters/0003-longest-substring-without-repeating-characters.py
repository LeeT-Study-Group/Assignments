class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = {}
        count = 0
        x = 0
        
        for i in range(len(s)):
            if s[i] in char and char[s[i]]>=x:
                x = char[s[i]]+1
            char[s[i]] = i
            count = max(count,i-x+1)
        
        return count
    