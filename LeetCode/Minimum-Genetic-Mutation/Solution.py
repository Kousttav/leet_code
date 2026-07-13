1from queue import Queue
2class Solution:
3    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
4        bank=set(bank)
5        if endGene not in bank:
6            return -1
7        visited=set()
8        q=Queue()
9        q.put((startGene,0))
10        g='ACGT'
11        while not q.empty():
12            gene,steps=q.get()
13            if gene==endGene:
14                return steps
15            for i in range(len(startGene)):
16                for ch in g:
17                    if ch==gene[i]:
18                        continue
19                    temp = gene[:i]+ch+gene[i+1:]
20                    if temp not in visited and temp in bank:
21                        visited.add(temp)
22                        q.put((temp,steps+1))
23        return -1