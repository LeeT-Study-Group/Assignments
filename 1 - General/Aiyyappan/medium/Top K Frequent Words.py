from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, (-freq, word))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result