1from queue import Queue
2class Solution:
3    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
4        bank=set(bank)
5        visited=set()
6        if endGene not in bank:
7            return -1
8        q=Queue()
9        q.put((startGene,0))
10        g='ACGT'
11        while not q.empty():
12            gene, steps = q.get()
13            if gene == endGene:
14                return steps
15
16            for i in range(len(startGene)):
17                for ch in g:
18                    if ch == gene[i]:
19                        continue
20                    temp = gene[:i] + ch + gene[i+1:]
21                    if temp in bank and temp not in visited:
22                        visited.add(temp)
23                        q.put((temp,steps+1))
24        return -1
25        