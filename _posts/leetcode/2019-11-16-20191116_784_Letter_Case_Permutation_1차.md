---
category: Leetcode
---

1. 문제 분석
  - string내의 alphabet 부분을 lowercase와 capitalcase로 바꿔서 만들 수 있는 모든 permutation을 반환하라.
  - DP문제로 추정.

2. Prerequisite
  - alphabet/number를 구분해야함. —> predefined 함수는? —> isalpha
  - cache 정의

3. 주의사항 Or 고려사항
  - cache를 어떻게 가져갈 것인가
  - string + 연산에서 걸릴 시간
  - vector push에서 걸릴 시간
  - cache의 구성에 따른 메모리 사용량

4. 일단 가장 쉬운 방법으로 구현.
  - cache 는 vector<vector<string>>으로.
  - DP형태로 접근하되, cache string은 새로 생성될 때마다 string + 연산을 통해 늘려감.
  - cache[I]도 크기를 미리 잡아두는 것이 아니라 필요할 때 push_back

5. 결과

28ms, 6.73%, 15.6MB, 5.88%
역시 생각대로 시간도 오래 걸리고 메모리 사용도 많음

```
class Solution {
private:
    vector<string> letterCasePermutation(string S, int pos) {
        if( pos >= len )
            return vector<string> ();
        
        if( cache[pos].size() > 0 )
            return cache[pos];
        
        int start = pos;
        while( !isalpha(S[pos] ) && pos < len ) 
            pos++;
        
        int len_prefix = pos - start + 1;
        string prefix = S.substr(start, len_prefix);
        vector<string> &ret = cache[start];
        
        if( pos == len ) {
            ret = vector<string>(1, prefix);
            return ret;
        }
        
        vector<string> v = letterCasePermutation(S, pos + 1);
        vector<char> c = vector<char>(2, 'a');
        c[0] = S[pos];
        c[1] = changeCase(c[0]);
        
        if( v.empty()) {
            for( int i = 0 ; i < 2; ++i ) {
                prefix[len_prefix-1] = c[i];
                ret.push_back(prefix);
            }
            return ret;
        }
        
        for( int i = 0 ; i < 2; ++i ) {
            prefix[len_prefix-1] = c[i];
            for( string p : v ) {
                cout<<prefix + p <<endl;
                ret.push_back(prefix + p);
            }
        }
        
        return ret;
    }
    vector<vector<string>> cache;
    int len;
    char changeCase(char c) {
        if( c < 'a' )
            return c + 32;
        return c - 32;
    }
public:
    vector<string> letterCasePermutation(string S) {
        len = S.size();
        if( len < 1 ) 
            return vector<string>();
        cache = vector<vector<string>>( len, vector<string>());
        return letterCasePermutation(S, 0);
    }
};
```
