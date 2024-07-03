class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = l = 0
        length = 0
        store = set()
        while r<len(s):
            if s[r] in store:
                length = max(length, r-l)
                while s[l] != s[r]:
                    store.remove(s[l])
                    l+=1
                l += 1
                r += 1
            else:
                store.add(s[r])
                r += 1
        length = max(length,r-l)
        return length