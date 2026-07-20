class Solution {
    public boolean isPalindrome(String s) {

        s = s.toLowerCase();
        char[] chars = s.toCharArray();
        int j = chars.length-1;
        int i = 0;
        while (i <= j) {
            while (i < j && !Character.isLetterOrDigit(chars[i])) {
                i++;
            }

            while (i < j && !Character.isLetterOrDigit(chars[j])) {
                j--;
            }

            if (chars[i] != chars[j]) {
                return false;
            }

            i++;
            j--;
        }
        return true;
    }
}
