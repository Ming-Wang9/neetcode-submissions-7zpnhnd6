class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([(beginWord, 1)])
        visited = set()
        wordset = set(wordList)
        while q:
            word, level = q.popleft()
            for i,c in enumerate(word):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    newword = word[:i]+letter+word[i+1:]
                    if newword not in visited and newword in wordset and newword!=word:
                        if newword == endWord:
                            return level+1
                        q.append([newword, level+1])
                        visited.add(newword)
        return 0