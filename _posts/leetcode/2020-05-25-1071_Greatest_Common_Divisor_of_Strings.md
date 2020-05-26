---
category: Leetcode
---

[greatest-common-divisor-of-strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

1. Problem Analysis
  - Find greatest common divisor of both string
  - both strings need to be consisted only by gcd
  
2. Prerequisite
  - If it is gauranteed that str1 and str2 always has some kind of order( ascending or descending ), code can be more simple and fast.

3. N.B

4. Plan
  - ~~Tried to use KMP.~~ Analyzed each string and find common. There were a lot of exceptions. 
  And most importantly, question asked about the gcd, so I didn't need to do that.
  - For the possible length of gcd, check the requirements ( see 1. Problem Analysis )
  - Because the question asked about gcd, trying from longest possible answer.
  
5. Result
  - 4ms. 96.31%, 7.1MB 100%

```cpp
class Solution {
private:
    bool compare(string s1, string s2, int t) {
        int len = s1.size();
        for( int i = 0 ; i < len ; i += t ) {
            for( int j = 0 ; j < t ; ++j ) {
                if( s1[i + j] != s2[j] )
                    return false;
            }
        }
        return true;
    }
public:
    string gcdOfStrings(string str1, string str2) {
        int len1 = str1.size();
        int len2 = str2.size();
        if( len2 > len1 )
            return gcdOfStrings(str2, str1);
        int len = len2;
        int lent;
        for(int div = 1; div <= len ; ++div) {
            lent = len / div;
            if( len1 % lent ) 
                continue;
            if( len2 % lent )
                continue;
            
            if( !compare(str1, str2, lent ))
                continue;
            
            if( !compare(str2, str1, lent ))
                continue;
            
            return str1.substr(0, lent);
        }
        return "";
    }
};
```
