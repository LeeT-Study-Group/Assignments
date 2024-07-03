class Solution:
    def findWords(self, words):
        r1 = list('qwertyuiop')
        r2 = list('asdfghjkl')
        r3 = list('zxcvbnm')
        
        ans = []
        
        for i in words:
            ll = i.lower()
            if self.ispos(ll, r1) or self.ispos(ll, r2) or self.ispos(ll, r3):
                ans.append(i)
        
        return ans
    
    def ispos(self, word, row):
        for i in word:
            if i not in row:
                return False
        return True
