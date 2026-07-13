import java.util.*;

class Solution {

    class Node {
        String gene;
        int steps;

        Node(String gene, int steps) {
            this.gene = gene;
            this.steps = steps;
        }
    }

    public int minMutation(String startGene, String endGene, String[] bank) {

        Set<String> bankSet = new HashSet<>(Arrays.asList(bank));

        if (!bankSet.contains(endGene))
            return -1;

        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(startGene, 0));

        Set<String> visited = new HashSet<>();
        visited.add(startGene);

        char[] chars = {'A', 'C', 'G', 'T'};

        while (!q.isEmpty()) {

            Node curr = q.poll();

            if (curr.gene.equals(endGene))
                return curr.steps;

            char[] arr = curr.gene.toCharArray();

            for (int i = 0; i < arr.length; i++) {

                char original = arr[i];

                for (char ch : chars) {

                    if (ch == original)
                        continue;

                    arr[i] = ch;
                    String newGene = new String(arr);

                    if (bankSet.contains(newGene) && !visited.contains(newGene)) {
                        visited.add(newGene);
                        q.offer(new Node(newGene, curr.steps + 1));
                    }
                }

                arr[i] = original;
            }
        }

        return -1;
    }
}