class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        i = len(digits) - 1
        while i >= 0 :
            if carry:
                carry = ((digits[i] + 1) == 10)
                digits[i] = (digits[i] + 1) % 10
            else:
                break
            i -= 1
        if carry :
            digits.insert(0,1)
        return digits