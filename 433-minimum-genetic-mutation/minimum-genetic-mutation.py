from queue import Queue
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank=set(bank)
        if endGene not in bank:
            return -1
        visited=set()
        q=Queue()
        q.put((startGene,0))
        g='ACGT'
        while not q.empty():
            gene,steps=q.get()
            if gene==endGene:
                return steps
            for i in range(len(startGene)):
                for ch in g:
                    if ch==gene[i]:
                        continue
                    temp = gene[:i]+ch+gene[i+1:]
                    if temp not in visited and temp in bank:
                        visited.add(temp)
                        q.put((temp,steps+1))
        return -1