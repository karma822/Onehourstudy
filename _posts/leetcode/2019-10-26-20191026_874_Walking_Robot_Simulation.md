---
category: Leetcode
---
1. 문제 분석.
  - command 확인
  - 가려는 위치가 obstacle을 포함하고 있는 지 확인
  - ~~목적지 까지 가면서 매 위치에서 distance 계산~~ obstacle에 막히거나 마지막 위치에 도달했을 때만 distance계산하여 업데이트
2. 필요한 preprocessing/variable.
  - 현재 로봇이 보는 direction
  - obstacle_map
3. obstacle map에 대한 고찰. ( 아직도 고민 중 )
  - map/vector<vector> 로 하며 메모리를 많이 잡아 먹고, min/max를 알아내기 위해 미리 한 번 data를 훑어봐야함.
  - unordered_map을 쓰면, key는 vector로 못 쓰니까 string으로 변환해서(x,y형태로) 하며 사용 가능. but, insert가 오래 걸리고, data를 찾아보는 비용이 map보다 큼.

결과

속도가 너무 느림(9.25%)

```
class Solution {
private:
    int dir;
    int path[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0}};// N, E, S, W
    int getdir( int c, int dir ) {
        if( c < -1 ) {
            dir = ( dir + 3 ) % 4;
        } else
            dir = ( dir + 1 ) % 4;
        return dir;
    }
    unordered_map<string, bool> make_obstacles_map( vector<vector<int>> & obstacles ) {
        unordered_map<string,bool> m;
        for( vector<int> obs: obstacles ) {
            m[to_string(obs[0]) + "," + to_string(obs[1])] = true;
        }
        return m;
    }
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        dir = 0;
        int distance = 0;
        int steps = 0;
        int pos[2] = {0, 0};
        int next_pos[2] = {0, 0};
        
        unordered_map<string, bool> obs_map = make_obstacles_map(obstacles);
        
        for( int c: commands ) {
            if( c < 0 ) {
                dir = getdir(c, dir);
                steps = 0;
            } else {
                steps = c;
                for( int i = 0 ; i < steps; ++i ) {
                    next_pos[0] = pos[0] + path[dir][0];
                    next_pos[1] = pos[1] + path[dir][1];
                    if( obs_map[to_string(next_pos[0]) + "," + to_string(next_pos[1])] )
                        break;
                    pos[0] = next_pos[0];
                    pos[1] = next_pos[1];
                }
                distance = max(distance, pos[0] * pos[0] + pos[1] * pos[1]);
            }
        }
        return distance;
    }
};
```
