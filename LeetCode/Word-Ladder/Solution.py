1from queue import Queue
2
3class Solution:
4    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
5
6        wordSet = set(wordList)
7
8        if endWord not in wordSet:
9            return 0
10
11        q = Queue()
12        q.put((beginWord, 1))
13
14        visited = {beginWord}
15        letters = "abcdefghijklmnopqrstuvwxyz"
16
17        while not q.empty():
18
19            word, steps = q.get()
20
21            if word == endWord:
22                return steps
23
24            for i in range(len(word)):
25                for ch in letters:
26
27                    if word[i] == ch:
28                        continue
29
30                    newWord = word[:i] + ch + word[i+1:]
31
32                    if newWord in wordSet and newWord not in visited:
33                        visited.add(newWord)
34                        q.put((newWord, steps + 1))
35
36        return 0