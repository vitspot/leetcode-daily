class Node:
        def __init__(self,c,end=False):
            self.child = {}
            self.c = c
            self.end = end
            
    class Trie:
        def __init__(self):
            self.root = Node("/")
            
        def insert(self,word):
            cur = self.root
            for c in word:
                if c not in cur.child: cur.child[c] = Node(c)
                cur = cur.child[c]
            cur.end = True
                    
    
    
    class Solution:
        def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
            lookup = Trie()
            for w in words:
                lookup.insert(w)
                
            def dfs(r,c,cur,word):
                if not (0<=r<n and 0<=c<m): return
                w = board[r][c]
                if w not in cur.child: return
                if cur.child[w].end:
                    ans.add(word+w)
                board[r][c] = " "
                dfs(r+1,c,cur.child[w],word+w)
                dfs(r-1,c,cur.child[w],word+w)
                dfs(r,c+1,cur.child[w],word+w)
                dfs(r,c-1,cur.child[w],word+w)
    
                board[r][c] = w
                
            n = len(board)
            m = len(board[0])
            ans = set()
            
            for r in range(n):
                for c in range(m):
                    dfs(r,c,lookup.root,"")
            
            return ans