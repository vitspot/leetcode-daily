class Solution {
    public:
        bool exist(vector<vector<char>>& board, string word) {
             int len = board.size(), ans =0;
            for(int i = 0; i<len;i++){
                for(int j=0; j<board[0].size();j++){
                    // if((board[i][j] == word.at(0)) && solve(board, i, j, 0, word))
                    //     return true;
                    ans += solve(i, j, word, board, 0);
                    if(ans > 0) return true;
                }
                
            }
            
        return false;
    
       }
        
        // bool solve (vector<vector<char>>& board, int i, int j, int count, string &word)
         int solve (int i, int j, string word, vector<vector<char>>& board, int count)
        {
           
             int found =0;
             if(i>=0 and j>=0 and i< board.size() and j < board[0].size() and word[count] == board[i][j] )
             {
                 char temp = word[count];
                 board[i][j] ='*';
                 
                 count++;
                 if(count == word.size()) found +=1;
             
                 else{
                     found += solve(i+1, j, word, board, count);
                     found += solve(i-1, j, word, board, count);
                     found += solve(i, j+1, word, board, count);
                     found += solve(i, j-1, word, board, count);
    
                 }
                 board[i][j] = temp;
                 
             }
             return found;
        
    }
    };