---
category: Leetcode
---

1. 문제 분석
  - NxN 좌표계에 (j, i)에 grid[i][j]개의 cube가 쌓여 있을 때 xy, xz, yz평면에 projection한 면적의 합을 반환하라.
  - cube는 1x1x1
  - 0 <= grid[i][j] <= 50 &&  1 <= i <= 50 && 1 <= j <= 50  —> 50x50x3 = 7500이라 int범위 내에서 항상 결과 값이 존재
  - xy projection은 grid[i][j]에서 number of occupied cells
  - xz projection fxz(j) =  max(grid[i][j]) for i
  - yz projection fyz(i) = max(grid[i][j]) for j
2. Prerequisite
  - fxz와 fyz를 구해~~두면 도움이 될 수도. —> 구지 안 해도 될 지도?~~두는 과정이 계산 중간과정으로 반드시 필요함.
  - i, j의 max가 50 이므로 미리 변수를 50개로 잡아두고 계산을 해도 될 것 같음.
  - 전체 면적을 저장하는 변수 필요함.
3. 주의사항 Or  고려사항 
  - ~코딩하면서 고민해봐야겠음. 딱히 떠오르지 않음.~
4. 결과
4ms 98.47%, 9.2MB 100%
```
class Solution {
public:
    int projectionArea(vector<vector<int>>& grid) {
        vector<int> fxz = vector<int>( 50, 0);
        vector<int> fyz = vector<int>( 50, 0);
        int sum = 0;
        int len = grid.size();
        for( int i = 0 ; i < len ; ++i ) {
            for( int j = 0 ; j < len ; ++j ) {
                if( grid[i][j] > 0 )
                    ++sum;
                fxz[j] = max( fxz[j], grid[i][j] );
                fyz[i] = max( fyz[i], grid[i][j] );
            }
        }
        
        for( int i = 0 ; i < len; ++i ) {
            sum += fxz[i];
            sum += fyz[i];
        }
        return sum;
    }
};
```
