class Solution:
        def exist(self, board: List[List[str]], word: str) -> bool:
            n = len(word)
            N = len(board)
            M = len(board[0])
            
            def dfs(x,y,i):
                if i == n: return True
                if not (0<=x<N and 0<=y<M): return False
                if board[x][y]!=word[i]: return False
                
                board[x][y] = '  '
                path = [(-1,0),(1,0),(0,-1),(0,1)]
                
                result = any(dfs(x+r,y+m,i+1) for r,m in path)
                board[x][y] = word[i]
                return result
            
            C,starts = Counter(word),[]
            for x in range(N):
                for y in range(M):
                    C[board[x][y]] -= 1
                    if board[x][y] == word[0]: starts.append((x,y))
                        
            if max(C.values())>0: return False
            for r,c in starts:
                if dfs(r,c,0): return True
            
            return False