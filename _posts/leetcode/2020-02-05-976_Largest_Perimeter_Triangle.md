---
category: Leetcode
---

https://leetcode.com/problems/largest-perimeter-triangle/

1. Problem Analysis
  - Find out maximum perimeter of available triangle from the inputs
  
2. Prerequisite
  - for the triangle, sum of any two side is always larget than the other --> will be used as one of conditions
  - sorting will be helpful

3. N.B
  - If sorting is not used, need to be verified with all 3 kinds of summation (x + y, x + z, y + z )

4. Plan
  - Sort input (e.g. A, B, C, D, E)
  - Pick candidate from largest numbers (C, D, E)
  - With candidate check whether they can make triangle. ( C + D > E )
  - If candidates cannot make triangle take next largest as candidate ( B, C, D )
  - Do it until find out available number set.
  - Return perimeter if found, if not return 0
  
5. Result
  - 48ms. 95.42%, 10.4MB 100%
  
```
class Solution {
public:
    int largestPerimeter(vector<int>& A) {
        sort(A.begin(), A.end());
        int len = A.size();
        int sum;
        for( int i = len - 3 ; i > -1 ; --i ) {
            sum = A[i] + A[i+1];
            if( A[i+2] < sum )
                return A[i+2] + sum;
        }
        return 0;
    }
};
```
