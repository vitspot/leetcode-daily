class Solution
{
public:
    string tictactoe(vector<vector<int>> &moves)
    {

        int RowA[3] = {0}, ColA[3] = {0}, RowB[3] = {0}, ColB[3] = {0};
        int DiagA1 = 0, DiagA2 = 0, DiagB1 = 0, DiagB2 = 0;

        bool A = true;
        for (auto &checki : moves)
        {
            int r = checki[0];
            int c = checki[1];

            if (A)
            {

                // all the situations for which the output will be A

                if (++RowA[r] == 3 || ++ColA[c] == 3 || (r == c && ++DiagA1 == 3) || (r + c == 2 && ++DiagA2 == 3))
                    return "A";
            }
            else
            {

                // all the situations for which the output will be B

                if (++RowB[r] == 3 || ++ColB[c] == 3 || (r == c && ++DiagB1 == 3) || (r + c == 2 && ++DiagB2 == 3))
                    return "B";
            }

            A = A ? false : true;
        }

        return moves.size() == 9 ? "Draw" : "Pending";
    }
};