---
category: Leetcode
---

[rank-transform-of-an-array](https://leetcode.com/problems/rank-transform-of-an-array/)

1. Problem Analysis
  - replace int value in array as it's rank.
  
2. Prerequisite
  - Nothing

3. N.B
  - Nothing

4. Plan
  - list up integer values without duplicate (keys)
  - sort keys
  - map key - rank
  - replace the value
  
5. Result
  - 196ms. 91.63%, 38.1MB 46.27%
```cpp
class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        int len = arr.size();
        if( len < 1 )
            return vector<int> ();
        
        vector<int> v(arr.begin(), arr.end());
        sort(v.begin(), v.end());
        
        unordered_map<int,int> m;
        m.reserve(len);
        int index = 1;
        m[v[0]] = index;
        for(int i = 1 ; i < len; ++i ) {
            if( v[i] != v[i-1] )
                index++;
            m[v[i]] = index;
        }
        
        for( int i = 0 ; i < len; ++i ) 
            arr[i] = m[arr[i]];
        return arr;
    }
};
```
