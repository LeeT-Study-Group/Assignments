public class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        int sLen = s.length();
        int pLen = p.length();
        
        if (sLen < pLen) {
            return result;
        }

        Map<Character, Integer> pCount = new HashMap<>();
        Map<Character, Integer> sCount = new HashMap<>();

        // Initialize the character count map for p
        for (int i = 0; i < pLen; i++) {
            pCount.put(p.charAt(i), pCount.getOrDefault(p.charAt(i), 0) + 1);
            sCount.put(s.charAt(i), sCount.getOrDefault(s.charAt(i), 0) + 1);
        }

        // Sliding window
        for (int i = 0; i <= sLen - pLen; i++) {
            if (i > 0) {
                // Remove the character going out of the window
                char charToRemove = s.charAt(i - 1);
                sCount.put(charToRemove, sCount.get(charToRemove) - 1);
                if (sCount.get(charToRemove) == 0) {
                    sCount.remove(charToRemove);
                }

                // Add the new character coming into the window
                char charToAdd = s.charAt(i + pLen - 1);
                sCount.put(charToAdd, sCount.getOrDefault(charToAdd, 0) + 1);
            }

            // Compare the current window's character count with p's character count
            if (sCount.equals(pCount)) {
                result.add(i);
            }
        }

        return result;
    }
}