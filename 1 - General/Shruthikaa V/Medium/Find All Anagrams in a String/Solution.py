from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_count = Counter()
        p_len = len(p)
        s_len = len(s)
        result = []

        if s_len < p_len:
            return result

        for i in range(p_len):
            s_count[s[i]] += 1
        for i in range(s_len - p_len + 1):
            if i > 0:
                s_count[s[i - 1]] -= 1
                if s_count[s[i - 1]] == 0:
                    del s_count[s[i - 1]]

                s_count[s[i + p_len - 1]] += 1
            if s_count == p_count:
                result.append(i)

        return result
