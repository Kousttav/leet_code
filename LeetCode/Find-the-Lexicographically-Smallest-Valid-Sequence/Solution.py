1class Solution:
2    def validSequence(self, word1: str, word2: str) -> List[int]:
3        power=1
4        i = len(word1)-1
5        j = len(word2)-1
6        cnt = 0
7        l = []
8        while i >= 0:
9            if j >= 0 and word1[i] == word2[j]:
10                cnt += 1
11                j -= 1
12            l.append(cnt)
13            i -= 1
14        visited = l[::-1]
15        j=0
16        res=[]
17        for i in range(len(word1)):
18            if j==len(word2):
19                break
20            if word1[i]!=word2[j] and power!=0 :
21                if i != len(word1)-1 and visited[i+1] >= len(word2)-j-1:
22                    power-=1
23                    j+=1
24                    res.append(i)
25                else:
26                    continue
27            elif word1[i]!=word2[j] and power==0:
28                continue 
29            else:
30                res.append(i)
31                j+=1
32        if len(res) != len(word2):
33            return []
34        return res
35
36        
37        