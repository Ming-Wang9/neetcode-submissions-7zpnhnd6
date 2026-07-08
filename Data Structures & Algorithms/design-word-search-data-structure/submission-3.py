class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isword = True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                if word[i] == ".":
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if word[i] not in cur.children:
                        return False
                cur = cur.children[word[i]]
            return cur.isword
        return dfs(0,self.root)
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
