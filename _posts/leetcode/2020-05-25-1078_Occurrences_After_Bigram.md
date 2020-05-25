---
category: Leetcode
---

[occurrences-after-bigram](https://leetcode.com/problems/occurrences-after-bigram/)

1. Problem Analysis
  - For the string including spaces, find all words followed after first and second
  
2. Prerequisite
  - separating sub module for compare and find next starting position might helpful.

3. N.B
  - With python or javascript, weparating words in string is much easier.
  - First words can placed after second word like a b a b with a as first and b as second word.
  In this case, the second a can be both first and third word.

4. Plan
  - There is no big plan.
  - Find first word and second word, and then push back third word
  
5. Result
  - 0ms. 100%, 7.5MB 100%

```cpp
class Solution {
private:
    bool compare(string s1, string s2, int from, int len, int slen) {
        bool found = true;
        int i;
        if( slen < from + len )
            return false;
        
        for( i = 0 ; i < len ; ++i ) {
            if( s1[ from + i ] != s2[i] ) {
                found = false;
                break;
            }
        }
        if( i == len )
            return true;
        
        if( found ) {
            if((i < len) && (s1[i] == ' '))
                return true;
        }
        return false;
    }
    
    int find_next_start(string s, int from, int len) {
        for( int i = from ; i < len ; ++i ) {
            if( s[i] == ' ')
                return i;
        }
        return len;
    }
public:
    vector<string> findOcurrences(string text, string first, string second) {
        bool f = false;
        bool s = false;
        int len = text.size();
        int lenf = first.size();
        int lens = second. size();
        vector<string> ret;
        int start = 0;
        for( int i = 0 ; i < len ; ++i ) {
            if( !f ) {
                if(compare(text, first, i, lenf, len )) {
                    f = true;
                    i += lenf;
                } else {
                    s = false;
                    i = find_next_start(text, i, len);
                }
            }
            else if( !s ) {
                if(compare(text, second, i, lens, len )) {
                    s = true;
                    i += lens;
                } else {
                    f = false;
                    i--;
                }
            }else {
                int len3 = find_next_start(text, i, len);
                ret.push_back(text.substr(i, len3 - i ));
                f = false;
                s = false;
                i--;
            }
        }
        return ret;
    }
};
```
