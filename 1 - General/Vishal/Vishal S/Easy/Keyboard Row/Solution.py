class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ls = []
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]
        for word in words:
            if word[0].lower() in rows[0]:
                row = 0
            elif word[0].lower() in rows[1]:
                row = 1
            else:
                row = 2
            
            inPlace = True
            for x in word:
                if x.lower() not in rows[row]:
                    inPlace = False
                    break
            
            if inPlace:
                ls.append(word)
        return ls