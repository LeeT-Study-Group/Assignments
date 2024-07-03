class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int templen = temperatures.length;
        int[] result = new int[templen];
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < templen; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int idx = stack.pop();
                result[idx] = i - idx;
            }
            stack.push(i);
        }
        
        return result;
    }
}