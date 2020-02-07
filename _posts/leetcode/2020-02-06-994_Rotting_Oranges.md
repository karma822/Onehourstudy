---
category: Leetcode
---

[rotting-oranges](https://leetcode.com/problems/rotting-oranges/)

1. Problem Analysis
  - When rotten orange spreads, find out minimum number of time to spoil all oranges
  - Orages map is given
  - If not possible return -1
  
2. Prerequisite
  - Queue will store position of rotten oranges
  - If four neighbor position changes are stored, they will be useful

3. N.B
  - It's possible there is no available way to rotting all
  - empty cell cannot be rotten

4. Plan
  - Count number of oranges
  - Push positions of rotten oranges to queue
  - Do propagation
  - With empty queue, number of rotten oranges are same with number of oranges then return minutes to do that.
  
5. Result
  - 4ms. 95.63%, 9.1MB 87.5%

<pre><code>int neighbor[4][2] = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int,int>> q;
        int w, h;
        int i, j;
        int count = 0;
        
        h = grid.size();
        w = grid[0].size();
        
        int rotten = 0;
        for( i = 0 ; i < h ; ++i ) {
            for( j = 0 ; j < w; ++j ) {
                if( grid[i][j] > 0 )
                    count++;
                if( grid[i][j] == 2 ) {
                    q.push(pair<int,int>(i, j));
                    rotten++;
                }
            }
        }
        
        pair<int,int> pos;
        int minutes = 0;
        int new_rotten = 0;
        int total = rotten;
        int x, y;
        
        while(!q.empty()) {
            pos = q.front();
            q.pop();
            for( i = 0 ; i < 4; ++i ) {
                y = pos.first + neighbor[i][0];
                x = pos.second + neighbor[i][1];
                if( x < 0 || x >= w || y < 0 || y >= h || grid[y][x] != 1 )
                    continue;
                q.push(pair<int,int>( y, x ));
                new_rotten++;
                grid[y][x] = 2;
            }
            rotten--;
            if( rotten < 1 ) {
                if( new_rotten > 0 )
                    minutes++;
                rotten = new_rotten;
                total += rotten;
                new_rotten = 0;
            }
        }
        
        if( total < count )
            return -1;
        
        return minutes;
    }
};
</code></pre>
