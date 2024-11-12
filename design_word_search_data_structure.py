#notes: 
#. == wildcard, have to check everything 
#same insert as usual trie
#use DFS to check for '.' cases with search

class TrieNode: 
    def __init__(self): 
        self.children = {}
        #keys: next chars, values: Trie nodes
        self.wordEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.wordEnd = True

    def search(self, word: str) -> bool:
        #keep track of index to see wordEnd
        def dfs(node, index): 
            if index == len(word): return node.wordEnd
            char = word[index]
            if char == '.': 
                for child in node.children.values():
                    if dfs(child, index + 1): return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)

        
        return dfs(self.root, 0)
