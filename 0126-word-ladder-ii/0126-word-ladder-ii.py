from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False
        letters = "abcdefghijklmnopqrstuvwxyz"

        while level and not found:
            nextLevel = set()

            for word in level:
                wordSet.discard(word)

            for word in level:
                for i in range(len(word)):
                    for ch in letters:
                        if word[i] == ch:
                            continue

                        newWord = word[:i] + ch + word[i+1:]

                        if newWord in wordSet:
                            parents[newWord].append(word)
                            nextLevel.add(newWord)

                            if newWord == endWord:
                                found = True

            level = nextLevel

        if not found:
            return []

        ans = []

        def dfs(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for parent in parents[word]:
                dfs(parent, path + [parent])

        dfs(endWord, [endWord])

        return ans