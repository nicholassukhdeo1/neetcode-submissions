class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]

        curr.word = True

        

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(start,curr):
            for index in range(start,len(word)):

                if word[index] == ".":
                    for child in curr.children.values():
                        # if dfs works.. 
                        if dfs(index+1, child):
                            return True
                        # if it doesn't.. return False.
                    return False
                else:
                    if word[index] not in curr.children:
                        return False
                    curr = curr.children[word[index]]
            if curr.word == True:
                return True
            else:
                return False

        return dfs(0,curr)

        
