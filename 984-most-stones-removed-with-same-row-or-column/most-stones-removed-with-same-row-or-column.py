class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(stones, idx, visited):
            visited[idx] = True

            r = stones[idx][0]
            c = stones[idx][1]

            for i in range(len(stones)):
                if not visited[i] and (stones[i][0] == r or stones[i][1] == c):
                    dfs(stones, i, visited)

        n = len(stones)
        components = 0
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue
            dfs(stones, i, visited)
            components += 1

        return n - components