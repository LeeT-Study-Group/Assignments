import java.util.*;

class Solution {
    public String[] findWords(String[] words) {
        String[] rows = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        List<String> result = new ArrayList<>();

        for (String word : words) {
            String lowerCaseWord = word.toLowerCase();
            char firstChar = lowerCaseWord.charAt(0);
            int row = getRow(firstChar, rows);
            boolean sameRow = true;

            for (int i = 1; i < lowerCaseWord.length(); i++) {
                char currentChar = lowerCaseWord.charAt(i);
                int rowCheck = getRow(currentChar, rows);
                if (rowCheck != row) {
                    sameRow = false;
                    break;
                }
            }

            if (sameRow) {
                result.add(word);
            }
        }

        return result.toArray(new String[result.size()]);
    }

    private int getRow(char c, String[] rows) {
        for (int i = 0; i < rows.length; i++) {
            if (rows[i].indexOf(c) != -1) {
                return i;
            }
        }
        return -1; 
    }
}
