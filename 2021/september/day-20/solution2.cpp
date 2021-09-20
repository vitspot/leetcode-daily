#include <bits/stdc++.h>
using namespace std;

string tictactoe(vector<vector<int>> &moves)
{
    if (moves.size() <= 2) return "Pending";

    int n = 3;
    vector<int> rows(3, 0);
    vector<int> cols(3, 0);
    int d1 = 0;
    int d2 = 0;

    int turnA = 1;
    for (auto i : moves) {
        int x = i[0];
        int y = i[1];

        rows[x] += turnA;
        cols[y] += turnA;

        if (x == y) d1 += turnA;
        if (x + y == n - 1) d2 += turnA;

        // check if its a winning condition
        if (
            abs(rows[x]) == n ||
            abs(cols[y]) == n ||
            abs(d1) == n ||
            abs(d2) == n)
        {
            return turnA == 1 ? "A" : "B";
        }
        turnA = -1 * turnA;
    }

    if (moves.size() < 9) return "Pending";
    return "Draw";
}