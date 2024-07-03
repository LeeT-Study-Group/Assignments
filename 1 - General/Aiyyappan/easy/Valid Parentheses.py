class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        b = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in b:
                top_element = stack.pop() if stack else '#'
                if b[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack