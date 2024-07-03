class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        int carry = 1;  

        for (int i = n - 1; i >= 0; i--) {
            int sum = digits[i] + carry;
            digits[i] = sum % 10;  
            carry = sum / 10;      
            
            if (carry == 0) {
                return digits;
            }
        }
        

        int[] result = new int[n + 1];
        result[0] = 1;  
        for (int i = 1; i < n + 1; i++) {
            result[i] = digits[i - 1];
        }
        
        return result;
    }