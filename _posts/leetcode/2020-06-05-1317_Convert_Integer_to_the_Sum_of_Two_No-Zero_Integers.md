---
category: Leetcode
---

[convert-integer-to-the-sum-of-two-no-zero-integers](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)

1. Problem Analysis
  - Find two integers without any zero in their digits whose sum is given number
  
2. Prerequisite
  - 2 <= n <= 10^4

3. N.B
  - Nothing

4. Plan
  - Get digits of given number
  - let a and b as digits for each integer at some position, then both a > 0 && b > 0 (except for the highest order of number)
  so let b = 1, then a = digit - b
  if a == 0 -> n -= 10, a = 9, b = 2
  if a < 0 -> n -= 10, a = 9
  - Store a and b somewhere
  - Make integer from digits
  
5. Result
  - 0ms. 100%, 6.2MB 53.75%

```cpp
class Solution {
private: 
    int reverse_num(int n) {
        int rev = 0;
        while( n > 0 ) {
            rev = rev * 10 + n % 10;
            n /= 10;
        }
        return rev;
    };
public:
    vector<int> getNoZeroIntegers(int n) {
        int a = 0;
        int b = 1;
        vector<int> ret(2, 0);
        int num = 0;
        
        if(n < 10) {
            ret[0] = n - 1;
            ret[1] = 1;
            return ret;
        }
        
        while( n > 9 ) {
            num = n % 10;
            b = 1;
            if( num > b ) {
                a = num - b;
            } else if( num == b ) {
                n -= 10;
                a = 9;
                b = 2;
            } else {
                n -= 10;
                a = 9;
            }
            ret[0] = ret[0] * 10 + a;
            ret[1] = ret[1] * 10 + b;
            n/= 10;
        }
        
        ret[0] = ret[0] * 10 + n;
        
        ret[0] = reverse_num(ret[0]);
        ret[1] = reverse_num(ret[1]);
        return ret;
    }
};
```
