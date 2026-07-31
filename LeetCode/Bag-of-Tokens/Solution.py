1class Solution:
2    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
3        n=len(tokens)
4        maxScore=0
5        i,j=0,n-1
6        tokens.sort()
7        score=0
8        while(i <=j):
9            if (power>=tokens[i]):
10                power-=tokens[i]
11                score+=1
12                i+=1
13                maxScore =max(maxScore,score)
14            elif score>=1:
15                power += tokens[j]
16                score-=1
17                j-=1
18            else:
19                return maxScore
20        return maxScore
21
22        