class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        power=1
        i = len(word1)-1
        j = len(word2)-1
        cnt = 0
        l = []
        while i >= 0:
            if j >= 0 and word1[i] == word2[j]:
                cnt += 1
                j -= 1
            l.append(cnt)
            i -= 1
        visited = l[::-1]
        j=0
        res=[]
        for i in range(len(word1)):
            if j==len(word2):
                break
            if word1[i]!=word2[j] and power!=0 :
                if i != len(word1)-1 and visited[i+1] >= len(word2)-j-1:
                    power-=1
                    j+=1
                    res.append(i)
                else:
                    continue
            elif word1[i]!=word2[j] and power==0:
                continue 
            else:
                res.append(i)
                j+=1
        if len(res) != len(word2):
            return []
        return res

        
        