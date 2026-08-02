from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[-1] * 501 for _ in range(501)]

        def solve(i, j):
            if i > j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            # Alex chooses the left pile
            choose_i = piles[i] + min(
                solve(i + 2, j),
                solve(i + 1, j - 1)
            )

            # Alex chooses the right pile
            choose_j = piles[j] + min(
                solve(i, j - 2),
                solve(i + 1, j - 1)
            )

            dp[i][j] = max(choose_i, choose_j)
            return dp[i][j]

        total = sum(piles)
        alex_score = solve(0, n - 1)

        return alex_score > total // 2