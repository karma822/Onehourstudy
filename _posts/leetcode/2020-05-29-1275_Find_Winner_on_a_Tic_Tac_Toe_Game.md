---
category: Leetcode
---

[find-winner-on-a-tic-tac-toe-game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)

1. Problem Analysis
  - Judge current status in tic-tac-toe game
  - **Do not guess anymore. Only judge current status.**
  
2. Prerequisite
  - Define enum for A, B, Draw, and Pending is helpful
  - Define direction by coordinate (rows, cols, and diags)
  - To share tic-tac-toe grid in functions, it is helpful to define grid in class member
  - For isolation and easy read, I made functions move(mark moves to grid), judge(judge status for each row/col/diag), count(count corresponding dir in grid)
  - inverse mapping from enum to string

3. N.B
  - **Again emphasizing, this problem is easy level. Do not presume any other than current status eventhough it is obvious you can guess winner form current status**

4. Plan
  - For every direction, count currently occupied cell and check is there any winner
  - If there is winner return winner
  - If there is no winner but there is still empty cell, return Pending
  - In other cases, return Draw
  
5. Result
  - 0ms. 100%, 8.8MB 100%

```cpp
enum WinType{
    EMPTY = 0,
    A = 1,
    B,
    DRAW,
    PENDING
};

vector<vector<vector<int>>> dir = {{{0, 0}, {0, 1}, {0, 2}}, 
                                   {{1, 0}, {1, 1}, {1, 2}}, 
                                   {{2, 0}, {2, 1}, {2, 2}}, 
                                   {{0, 0}, {1, 0}, {2, 0}}, 
                                   {{0, 1}, {1, 1}, {2, 1}}, 
                                   {{0, 2}, {1, 2}, {2, 2}},
                                   {{0, 0}, {1, 1}, {2, 2}}, 
                                   {{0, 2}, {1, 1}, {2, 0}}};

map<int, string> num_map = {{1, "A"}, {2, "B"}, {4, "Pending"}};
class Solution {
private:
    vector<vector<int>>m;
    WinType judge(vector<int> &count) {
        if( count[A] + count[B] < 3 )
            return PENDING;
        else if( count[ A ] > 0 && count[ B ] > 0 )
            return DRAW;
        else if( count[ A ] == 3 )
            return A;
        else if( count[ B ] == 3 )
            return B;
        else
            return PENDING;
    };
    
    void move(int x, int y, int turn) {
        m[y][x] = turn;
    };
    
    vector<int> count_line(vector<vector<int>> &d) {
        vector<int> count(3, 0);
        for( vector<int> &pair : d ) {
            count[m[pair[1]][pair[0]]]++;
        }
        return count;
    }
    
public:
    string tictactoe(vector<vector<int>>& moves) {
        m = vector<vector<int>>(3, vector<int>(3, 0));
        int turn = A;
        for( vector<int> &m : moves ) {
            move(m[1], m[0], turn);
            turn = 3 - turn;
        }
        
        vector<int> possibility(5, EMPTY);
        
        int i = 0;
        bool pending = false;
        for( vector<vector<int>> &d : dir ) {
            vector<int> count = count_line(d);
            int j = judge(count);
            if( j < DRAW )
                return num_map[j];
            if( j == PENDING ) {
                pending = true;
            }
        }
        
        if( pending )
            return "Pending";
        return "Draw";
    }
};
```
