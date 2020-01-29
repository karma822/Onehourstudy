---
category: Leetcode
---

https://leetcode.com/problems/verifying-an-alien-dictionary/

1. Problem Analysis
  - Decide whether the words are in order of an alien dictionary
  
2. Prerequisite
  - dictionary map( alphabet-index ) need to be stored in cache/heap

3. N.B
  - dictionary doesn't need to be variable. It's maximum size is 26, so make it fixed-size.
  - It could there is only one words then it is always in order.

4. Plan
  - make map with given dictionary string.
  - compare adjacent words' order

5. Result
  - 4ms. 96.60%, 9.1MB 92.31%
  
```
class Solution {
private:
    vector<int> m;
    int dic_size;
    bool is_in_order(string &s1, string &s2) {
        int len1 = s1.size();
        int len2 = s2.size();
        int len = min(len1, len2);
        
        for( int i = 0 ; i < len; ++i ) {
            if( s1[i] != s2[i] ){
                if( m[s1[i]- 'a'] > m[s2[i] - 'a'] )
                    return false;
                else
                    return true;
            }
        }
        
        if( len1 > len2 )
            return false;
        return true;
    }
    
public:
    bool isAlienSorted(vector<string>& words, string order) {
        int number_words = words.size();
        if( number_words < 2 )
            return true;
        
        m = vector<int>(26, -1);
        dic_size = order.size();
        for( int i = 0 ; i < dic_size; ++i ) {
            m[order[i] - 'a'] = i;
        }
        
        for( int i = 1 ; i < number_words; ++i ) {
            if( !is_in_order(words[i-1], words[i]))
                return false;
        }
        return true;
    }
};
```
