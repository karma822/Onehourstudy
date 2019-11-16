---
category: Leetcode
---

분석 부분은 https://karma822.github.io/Onehourstudy/20191116_784_Letter_Case_Permutation_1차/ 참조

4. 일단 string 연산을 줄여보자
  - string의 최종 길이를 알고 있음. —> string + 연산을 쓰지 말고 position에 덮어 씀.

5. 결과

12ms, 54.07%, 15.9MB, 5.88%
생각보다 메모리 사용량은 많이 안 늘고 시간은 줄어들었음.
Queue나 Stack으로도 왠지 접근이 가능할 것 같은데, 고민 좀 해봐야겠다..

```
class Solution {
private:
    vector<string> letterCasePermutation(string S, int pos) {
        if( pos >= len )
            return vector<string> ();
        
        if( cache[pos].size() > 0 )
            return cache[pos];
        
        vector<string> &ret = cache[pos];
        
        vector<string> v = letterCasePermutation(S, pos + 1);
        
        vector<char> c;
        int number_char = 0;
        if( isalpha(S[pos])) {
            number_char = 2;
            c = vector<char>(number_char, S[pos]);
            c[1] = changeCase(c[0]);
        } else {
            number_char = 1;
            c = vector<char>(number_char, S[pos]);
        }
        
        if( v.empty()) {
            for( int i = 0 ; i < number_char; ++i ) {
                string s = string(S);
                s[len - 1] = c[i];
                ret.push_back(s);
            }
            return ret;
        }
        
        for( int i = 0 ; i < number_char; ++i ) {
            for( string p : v ) {
                p[pos] = c[i];
                ret.push_back(p);
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
