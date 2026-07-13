1from collections import defaultdict, deque
2from typing import List
3
4class Solution:
5    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
6
7        wordSet = set(wordList)
8
9        if endWord not in wordSet:
10            return []
11
12        parents = defaultdict(list)
13        level = {beginWord}
14        found = False
15        letters = "abcdefghijklmnopqrstuvwxyz"
16
17        while level and not found:
18            nextLevel = set()
19
20            for word in level:
21                wordSet.discard(word)
22
23            for word in level:
24                for i in range(len(word)):
25                    for ch in letters:
26                        if word[i] == ch:
27                            continue
28
29                        newWord = word[:i] + ch + word[i+1:]
30
31                        if newWord in wordSet:
32                            parents[newWord].append(word)
33                            nextLevel.add(newWord)
34
35                            if newWord == endWord:
36                                found = True
37
38            level = nextLevel
39
40        if not found:
41            return []
42
43        ans = []
44
45        def dfs(word, path):
46            if word == beginWord:
47                ans.append(path[::-1])
48                return
49
50            for parent in parents[word]:
51                dfs(parent, path + [parent])
52
53        dfs(endWord, [endWord])
54
55        return ans