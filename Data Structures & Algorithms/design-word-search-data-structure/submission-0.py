class WordDictionary:

    def __init__(self):
        self.arr = []

    def addWord(self, word: str) -> None:
        self.arr.append(word)

    def search(self, word: str) -> bool:
        for w in self.arr:
            if len(w) != len(word):
                continue
            match = True
            for c1, c2 in zip(word, w):
                if c1 != '.' and c1 != c2:
                    match = False
                    break
            if match:
                return True
        return False
