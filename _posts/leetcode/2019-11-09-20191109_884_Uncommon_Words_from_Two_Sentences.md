---
category: Leetcode
---
1. 문제 분석
  - 기본 내용은 https://karma822.github.io/Onehourstudy/20191104_884_Uncommon_Words_from_Two_Sentences/ 참조
  - trie로 풀어보기로 함
2. Prerequisite
  - Trie class 구현
  - Trie traverse 구현
  - trie vs word 비교함수 구현
  - hashmap에 word와 나온 횟수 저장
3. 주의사항 Or 고려사항
  - 필요한 data structure가 지원 안 되서 신규로 구현할 때, 기본 포맷은 익히고 있어야 함. (기억 안 나서..ㅠ)
  - Trie 특성
  - word traverse할 때 인덱스 
4. 구현 결과
8ms 7.16%, 11.4MB 12.50%
왜 더 느려지고 메모리도 더 많이 쓰는 건지-_-;
- word 만드는 부분에 좀 더 신경을 써 보면 좋을 듯.
- trie를 썼는 데 구지 hashmap 까지 필요할까? 이부분에 있어서 더 좋은 접근을 생각해보면 좋을 듯.
- trie에 child 노드를 그냥 최대 27개로 한정 지어두고 length를 따로 저장하고 있는 것도 속도 향상에는 좋을 듯.. (지금은 push_back이라 오래 걸리는 거 같음)

```
class TrieNode {
public:
    char val;
    vector<TrieNode*> child;
    TrieNode( char c) {
        val = c;
        child = vector<TrieNode*> ();
    };
};

class Solution {
private:
    TrieNode *root;
    bool traverse_child( TrieNode *node, char c) {
        int len = node->child.size();
        for( int i = 0 ; i < len; ++i ) {
            if( node->child[i]->val == c ) {
                node = node->child[i];
                return true;
            }
        }
        return false;
    }
    
    bool search( TrieNode *head, string word, int *start) {
        int len = word.size();
        for( ; *start < len; ++(*start) ) {
            if( word[*start] == ' ' ) //end of the word
                break;
            bool found = traverse_child(head, word[*start]);
            if( found )
                continue;
            else
                return false;
        }
        
        if( traverse_child(head, '*'))
            return false;
        
        return true;
    }
    
    string make_word(string str, int start, int end) {
        int len = end - start;
        string s = string(len, 'a');
        for( int i = 0 ; i < len; ++i ) {
            s[i] = str[start+i];
        }
        return s;
    }
    
    unordered_map<string, int> hashmap;
    
    bool registerword(string word, int *start) {
        int len = word.size();
        TrieNode *head = root;
        int started = *start;
        bool result = search(head, word, start);
        int end;
        if( result ) {
            end = *start;
            hashmap[make_word(word, started, end)]++;
            return false;
        }
        
        for( ; *start < len; ++(*start) ) {
            if( word[*start] == ' ' ) //end of the word
                break;
            int child_len = head->child.size();
            head->child.push_back(new TrieNode(word[*start]));
            head = head->child[child_len];
        }
        head->child.push_back(new TrieNode('*'));
        end = *start;
        hashmap[make_word(word, started, end)]++;
        return true;
    };
    
    int wordcount = 0;
    void registerwords( string str ) {
        int len = str.size();
        for( int i = 0 ; i < len; ++i ) {
            bool result = registerword( str, &i );
        }
    };
    
    vector<string> get_uncommon() {
        vector<string> ret(hashmap.size(), "");
        int ret_size = 0;
        for( unordered_map<string, int>::iterator it = hashmap.begin(); it != hashmap.end(); ++it ) {
            if( it->second < 2 )
                ret[ret_size++] = it->first;
        }
        ret.resize(ret_size);
        return ret;
    }
public:
    vector<string> uncommonFromSentences(string A, string B) {
        root = new TrieNode('*');
        registerwords(A);
        registerwords(B);
        return get_uncommon();
    }
};
```
