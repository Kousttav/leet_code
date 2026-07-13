from queue import Queue
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank=set(bank)
        visited=set()
        if endGene not in bank:
            return -1
        q=Queue()
        q.put((startGene,0))
        g='ACGT'
        while not q.empty():
            gene, steps = q.get()
            if gene == endGene:
                return steps

            for i in range(len(startGene)):
                for ch in g:
                    if ch == gene[i]:
                        continue
                    temp = gene[:i] + ch + gene[i+1:]
                    if temp in bank and temp not in visited:
                        visited.add(temp)
                        q.put((temp,steps+1))
        return -1
        