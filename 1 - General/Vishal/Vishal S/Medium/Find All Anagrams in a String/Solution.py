class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        def build(string):
            arr = [0]*26
            for x in string:
                arr[ord(x)-ord('a')]+=1
            return arr
        
        def compare(arr1,arr2):
            for i in range(26):
                if arr1[i]!=arr2[i]:
                    return False
            return True
        p_len, s_len = len(p), len(s)
        result = []
        p_count = build(p)
        s_count = build(s[0:p_len])
        if compare(s_count,p_count):
            result.append(0)
        for i in range(1,s_len-p_len+1):
            s_count[ord(s[i-1])-ord('a')]-=1
            s_count[ord(s[i+p_len-1])-ord('a')]+=1
            if compare(s_count,p_count):
                result.append(i)
        return result