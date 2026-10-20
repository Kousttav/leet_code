class Solution {
    public String removeStars(String s) {
        char[] stack = new char[s.length()];
        int top = -1;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch == '*') {
                top--;
            } else {
                top++;
                stack[top] = ch;
            }
        }

        return new String(stack, 0, top + 1);
    }
}