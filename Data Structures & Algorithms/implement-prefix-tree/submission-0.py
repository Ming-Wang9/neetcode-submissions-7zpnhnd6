class PrefixTree:

    def __init__(self):
        self.arr = []

    def insert(self, word: str) -> None:
        self.arr.append(word)

    def search(self, word: str) -> bool:
        return word in self.arr

    def startsWith(self, prefix: str) -> bool:
        for word in self.arr:
            if word.startswith(prefix):
                return True
        return False
        
        