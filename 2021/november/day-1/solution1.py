class Solution:
        def solve(self, board: List[List[str]]) -> None:
            def dfs(x,y):
                if not (0<=x<n and 0<=y<m) or board[x][y]!='O':
                    return
                board[x][y] = 'S'
                dfs(x+1,y) ; dfs(x-1,y) # up and down
                dfs(x,y+1) ; dfs(x,y-1) # left and right
                
            n = len(board) # no of rows
            m = len(board[0]) # no of column
            
            # Looping throw the first and last column to find 'O'
            for i in range(n):
                dfs(i,0)
                dfs(i,m-1)
            
            # Looping throw the first and last row to find 'O'
            for j in range(m):
                dfs(0,j)
                dfs(n-1,j)
            
            # Now Change the 'S' that are in borders to 'O'
            
            # Changin the 'S' in first and last column to 'O'
            for i in range(n):
                if board[i][0] == 'S': board[i][0] = 'O'
                if board[i][m-1] == 'S': board[i][m-1] = 'O'
                    
            # Changin the 'S' in first and last row to 'O'
            for j in range(m):
                if board[0][j] == 'S': board[0][j] = 'O'
                if board[n-1][j] == 'S': board[n-1][j] = "O"
                    
            """
            Now all the 'S' which are inside the border are not surrounded 
            by X, so change it to 'O' and rest of the 'O' can be 
            converted to 'X' as it is surrounded by 'X'
            """
            
            for i in range(1,n-1):
                for j in range(1,m-1):
                    if board[i][j] == 'O': board[i][j] = "X"
                    if board[i][j] == "S": board[i][j] = "O"