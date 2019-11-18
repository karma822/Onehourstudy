---
category: Leetcode
---


1. 문제 분석
  - string s가 주어지고 각 char의 width가 주어질 때, s 내의 char 순서대로 line을 채운다.
  - 각 라인은 최대 100의 width를 가지며, 이를 초과하는 char가 나올 경우 다음 line으로 변경한다.
  - s의 char 순서대로 width를 더해서 100을 넘는 순간 line + 1 , occupied 초기화 —> line 과 occupied를 반환하면 됨.

2. Prerequisite
  - char to int mapping ( index 접근에 용이하도록 )

3. 주의사항 Or 고려사항
  - char는 low case only
  - 2 <= widths[I] <=10

4. 구현 방안
  - brute-force

5. 결과

0ms 100%, 8.6MB 100%

```
class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string S) {
        vector<int> ret = vector<int> (2, 0);
        if( S.size() < 1 ) {
            return ret;
        }
        
        int line = 1;
        int occupied = 0;
        int len = S.size();
        for( int i = 0 ; i < len; ++i ) {
            int w = widths[S[i] - 'a'];
            if( occupied + w > 100 ){
                line++;
                occupied = 0;
            }
            occupied += w;
        }
        ret[0] = line;
        ret[1] = occupied;
        return ret;
    }
};
```
