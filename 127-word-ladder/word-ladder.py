from queue import Queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = Queue()
        q.put((beginWord, 1))

        visited = {beginWord}
        letters = "abcdefghijklmnopqrstuvwxyz"

        while not q.empty():

            word, steps = q.get()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in letters:

                    if word[i] == ch:
                        continue

                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        q.put((newWord, steps + 1))

        return 0