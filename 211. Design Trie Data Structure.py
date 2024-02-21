class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]

        node['#'] = True

    def search(self, word: str) -> bool:
        
        def sub_search(word,node):
            for i,ch in enumerate(word):
                if not ch in node:
                    if ch == '.':
                        for x in node:
                            if x !='#' and sub_search(word[i+1:],node[x]):
                                return True
                    return False
                else:
                    node = node[ch]
            return '#' in node
        return sub_search(word,self.trie)
