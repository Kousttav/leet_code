class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n=len(tokens)
        maxScore=0
        i,j=0,n-1
        tokens.sort()
        score=0
        while(i <=j):
            if (power>=tokens[i]):
                power-=tokens[i]
                score+=1
                i+=1
                maxScore =max(maxScore,score)
            elif score>=1:
                power += tokens[j]
                score-=1
                j-=1
            else:
                return maxScore
        return maxScore

        