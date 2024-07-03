class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def divideWords():
            result = []
            curr = [words[0]]
            length = len(words[0])
            count = 1
            for x in words[1:]:
                if length + count + len(x) <= maxWidth: 
                    length += len(x)
                    curr.append(x)
                    count += 1
                else:
                    result.append((curr,maxWidth - length))
                    curr = [x]
                    length = len(x)
                    count = 1
            result.append((curr, maxWidth - length))
            return result

        def justify(data):
            for i in range(len(data)-1):
                divs = len(data[i][0]) - 1
                if divs == 0:
                    data[i] = data[i][0][0]+ " "*(data[i][1])
                    continue
                spaces = data[i][1] // divs
                filler = data[i][1] - divs*spaces
                txt = data[i][0][0]
                for x in data[i][0][1:]:
                    txt += " " * (spaces)
                    if filler:
                        txt += " "
                        filler -= 1                        
                    txt += x
                data[i] = txt
            data[-1] = " ".join(data[-1][0]) + " " * (data[-1][1]-len(data[-1][0])+1)
            return data
        
        return justify(divideWords())