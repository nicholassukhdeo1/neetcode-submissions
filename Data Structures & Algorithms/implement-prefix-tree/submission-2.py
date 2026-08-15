class TrieNode:
    def __init__(self):
        self.children = {}
        # does this letter signal the end of a word?
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # we add nodes of letters starting at the root
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]

        curr.word = True


    def search(self, word: str) -> bool:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        return curr.word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        # return True instead of curr.word because not guaranteed that this letter signals
        # the end of the word.
        return True

    
        
        