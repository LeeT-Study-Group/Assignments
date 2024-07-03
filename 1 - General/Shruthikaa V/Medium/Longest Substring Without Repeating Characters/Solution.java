class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> charIndexMap = new HashMap<>();
        int left = 0;
        int maxlength = 0;

        for(int right = 0;right<s.length();right++){
            char current = s.charAt(right);
            if(charIndexMap.containsKey(current)&& charIndexMap.get(current)>=left){
                left = charIndexMap.get(current)+1;
            }
            charIndexMap.put(current,right);
            maxlength = Math.max(right-left+1, maxlength);
        }
        


    return maxlength;    
    }
     
}