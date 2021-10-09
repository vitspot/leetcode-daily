class Node:
        def __init__(self,c,end=False):
            self.c = c
            self.child = {}
            self.end = end
            
    class Trie:
    
        def __init__(self):
            self.root = Node("/")
    
        def insert(self, word: str) -> None:
            cur = self.root
            for c in word:
                if c not in cur.child: cur.child[c] = Node(c)
                cur = cur.child[c]
            cur.end = True
    
        def search(self, word: str) -> bool:
            cur = self.root
            for c in word:
                if c not in cur.child: return False
                cur = cur.child[c]
            return cur.end
    
        def startsWith(self, prefix: str) -> bool:
            cur = self.root
            for c in prefix:
                if c not in cur.child: return False
                cur = cur.child[c]
            return True
    
    
    # Your Trie object will be instantiated and called as such:
    # obj = Trie()
    # obj.insert(word)
    # param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)