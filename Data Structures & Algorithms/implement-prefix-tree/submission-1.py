class TrieNode: 
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        i = self.root
        for char in word:
            if char not in i.children:
                i.children[char] = TrieNode()
            i = i.children[char]
        i.endOfWord = True

    def search(self, word: str) -> bool:
        i = self.root
        for char in word: 
            if char not in i.children:
                return False
            i = i.children[char]
        return i.endOfWord

    def startsWith(self, prefix: str) -> bool:
        i = self.root
        for char in prefix:
            if char not in i.children:
                return False
            i = i.children[char]
        return True
        