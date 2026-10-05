1import java.util.*;
2
3class Solution {
4    public boolean isValid(String s) {
5        Stack<Character> st = new Stack<>();
6        HashMap<Character, Character> map = new HashMap<>();
7
8        map.put(')', '(');
9        map.put('}', '{');
10        map.put(']', '[');
11
12        for (char ch : s.toCharArray()) {
13
14            if (!map.containsKey(ch)) {
15                st.push(ch);
16            } else {
17                if (st.isEmpty() || st.pop() != map.get(ch)) {
18                    return false;
19                }
20            }
21        }
22
23        return st.isEmpty();
24    }
25}