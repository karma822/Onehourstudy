---
category: Leetcode
---

https://leetcode.com/problems/delete-columns-to-make-sorted/

1. Problem Analysis
  - Count the number of columns to make all columns are sorted as ascending order
  
2. Prerequisite
  - Nothing

3. N.B
  - ascending order includes same values in order

4. Plan
  - check the column by indexes looping and count number of column not in ascending order

5. Result
  - 52ms. 96.43%, 13.1MB 71.43%
  
```
class Solution {
public:
    int minDeletionSize(vector<string>& A) {
        int num = A.size();
        int len = A[0].size();
        int count = 0;
        int i, j;
        for( i = 0 ; i < len; ++i ) {
            for( j = 1 ; j < num; ++j ) {
                if( A[j][i] < A[j-1][i] ) {
                    ++count;
                    break;
                }
            }
        }
        return count;
    }
};
```
