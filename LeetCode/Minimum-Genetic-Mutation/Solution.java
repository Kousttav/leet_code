1import java.util.*;
2
3class Solution {
4
5    class Node {
6        String gene;
7        int steps;
8
9        Node(String gene, int steps) {
10            this.gene = gene;
11            this.steps = steps;
12        }
13    }
14
15    public int minMutation(String startGene, String endGene, String[] bank) {
16
17        Set<String> bankSet = new HashSet<>(Arrays.asList(bank));
18
19        if (!bankSet.contains(endGene))
20            return -1;
21
22        Queue<Node> q = new LinkedList<>();
23        q.offer(new Node(startGene, 0));
24
25        Set<String> visited = new HashSet<>();
26        visited.add(startGene);
27
28        char[] chars = {'A', 'C', 'G', 'T'};
29
30        while (!q.isEmpty()) {
31
32            Node curr = q.poll();
33
34            if (curr.gene.equals(endGene))
35                return curr.steps;
36
37            char[] arr = curr.gene.toCharArray();
38
39            for (int i = 0; i < arr.length; i++) {
40
41                char original = arr[i];
42
43                for (char ch : chars) {
44
45                    if (ch == original)
46                        continue;
47
48                    arr[i] = ch;
49                    String newGene = new String(arr);
50
51                    if (bankSet.contains(newGene) && !visited.contains(newGene)) {
52                        visited.add(newGene);
53                        q.offer(new Node(newGene, curr.steps + 1));
54                    }
55                }
56
57                arr[i] = original;
58            }
59        }
60
61        return -1;
62    }
63}