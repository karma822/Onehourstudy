---
category: Leetcode
---

https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

1. Problem Analysis 1
  - Find out one repeating item in array with size 2*N and one item is repeating N times
  
2. Prerequisite
  - Nothing

3. N.B
  - Nothing

4. Plan 1
  - Count occurrence in hashmap
  - If one item in hashmap is larger than 0 before counted, then return that item
  
5. Result 1
  - 44ms. 59.85%, 10.8MB 40%
  
```
class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
        unordered_map<int, int> count;
        for( auto i : A ) {
            if( count[i] > 0 )
                return i;
            count[i] = 1;
        }
        return -1;//somethign wrong
    }
};
```

1. Problem Analysis 2
  - By definition of problem, half of the numbers are the one repeating.
  - As a result, at least two of repeating number should be placed at most one different number apart. (e.g. at least two x should be placed like  x y x )
  
4. Plan 2
  - By traversing through array, check any number is repeating in distance less than 3.
  - If there is nothing repeated until len-2, than there are only two cases. x y z x or y z x x. So either case A[len-1] is the answer
  
5. Result 2
  - 44ms. 59.85%, 10.7MB 80% what happen with those 40%?
  
```
class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
        int len = A.size();
        
        for( int i = 0 ; i < len - 2; ++i ) {
            if( A[i] == A[i+1] || A[i] == A[i+2])
                return A[i];
        }
        return A[len-1];
    }
};
```
