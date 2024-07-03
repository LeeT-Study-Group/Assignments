class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dictf = {}
        for word in words:
            dictf[word] = dictf.get(word,0)+1
        
        ans = list(dictf.keys())
        ans.sort(key=lambda x: (-dictf[x], x))
        
        return ans[:k]