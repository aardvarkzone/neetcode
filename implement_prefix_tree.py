class TrieNode: 
    #each node represents a character
    #each node has an option for wordEnd - 
    #meaning even if it has children for some other word,
    #you can still just have the word end too (like apple and app both being valid)
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.wordEnd = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char in current.children: 
                current = current.children[char]
            else: return False
        return current.wordEnd

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix: 
            if char in current.children: 
                current = current.children[char]
            else: return False
        return True
        
        
