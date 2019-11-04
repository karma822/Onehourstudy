---
category: Leetcode
---
1. 문제 분석
  - 주어진 두개의 문장에서 한번 만 등장하는 모든 단어를 return 하면 됨.
  - 문장은 space separated 단어들의 집합
  - hashmap 100%
  - 단어 분리하는 게 있으니, stack 혹은 queue?
  - trie 로 될 지도? —> 이쪽 접근 방법으로 풀어볼 필요도 있음. 
  - 일단은 queue를 이용 해 단어 분리 후 접근.
2. Prerequisite
  - 문장에서 단어 분리하는 함수필요 —> python은 매우 쉽게 되는데… 흠..
  - hashmap 만드는 함수는 따로 빼면 코드가 좀 더 깨끗해질 듯..
3. 주의사항 Or 고려사항
  - 기억속으로 잊혀진 c++문법 주의..
4. 결과
4ms 70.20%, 9.7MB 12.50%
easy치고 코드가 너무 길어진 듯..
trie로 다시 한번 해 봐야할 듯..
```
class Solution {
private:
    vector<string> extract_words(string s) {
        queue<char> q_char;
        int len = s.size();
        vector<string> ret(len, "");
        int ret_len = 0;
        for( int i = 0; i < len; ++i ) {
            if( s[i] != ' ' ) {
                q_char.push(s[i]);
            } else {
                string word = "";
                while( !q_char.empty()) {
                    word += q_char.front();
                    q_char.pop();
                }
                ret[ret_len++] = word;
            }
        }
        string word = "";
        while( !q_char.empty()) {
            word += q_char.front();
            q_char.pop();
        }
        if( word.size() > 0 )
            ret[ret_len++] = word;
        
        ret.resize(ret_len);
        return ret;
    }
    unordered_map<string, int> get_hashmap(vector<string> &words) {
        int len = words.size();
        unordered_map<string, int> m;
        for( int i = 0 ; i < len ; ++i ) {
            m[words[i]]++;
        }
        return m;
    }
public:
    vector<string> uncommonFromSentences(string A, string B) {
        vector<string> words_A = extract_words(A);
        vector<string> words_B = extract_words(B);
        unordered_map<string, int> hashmap_A = get_hashmap(words_A);
        unordered_map<string, int> hashmap_B = get_hashmap(words_B);
        vector<string> uncommon( hashmap_A.size() + hashmap_B.size(), "");
        int len = 0;
        for( unordered_map<string, int>::iterator it = hashmap_A.begin(); it != hashmap_A.end(); ++it ) {
            if( it->second < 2 && hashmap_B[it->first] < 1 ) {
                uncommon[len++] = it->first;
            }
        }
        for( unordered_map<string, int>::iterator it = hashmap_B.begin(); it != hashmap_B.end(); ++it ) {
            if( it->second < 2 && hashmap_A[it->first] < 1 ) {
                uncommon[len++] = it->first;
            }
        }
        uncommon.resize(len);
        return uncommon;
    }
};
```
