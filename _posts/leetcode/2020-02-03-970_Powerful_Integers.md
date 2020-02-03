---
category: Leetcode
---

https://leetcode.com/problems/powerful-integers/

1. Problem Analysis
  - Find out all powerful integers with two input number
  
2. Prerequisite
  - Faster with memorization of powers
  - maximum memory needed when the input is 2, x, and 10^6 --> 21 for each

3. N.B
  - Care about the boundary

4. Plan
  - Calculate powers of each
  - for the powers from small to big, add the values
  - check the boundary
  
5. Result
  - 0ms. 100%, 8.6MB 55.56%
  
```
class Solution {
private:
    vector<int> get_powers(int x, int bound) {
        if( x <2 )
            return vector<int>(1, 1);
        
        vector<int> powers(21, 1);
        int value = 1;
        int num = 1;
        for( int i = 1; value < bound; ++i ) {
            value *= x;
            powers[i] = value;
            num++;
        }
        powers.resize(num);
        return powers;
    }
public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
        unordered_set<int> powerful;
        vector<int> powerfulx, powerfuly;
        int i, j;
        int valuex = 1, valuey = 1, sumpart = 1;
        
        powerfulx = get_powers(x, bound);
        powerfuly = get_powers(y, bound);
        
        int sum;
        int len1 = powerfulx.size();
        int len2 = powerfuly.size();
        for( int i = 0 ; i < len1 ; ++i ) {
            for( int j = 0 ; j < len2; ++j ) {
                sum = powerfulx[i] + powerfuly[j];
                if( sum <= bound )
                    powerful.insert(sum);
                else break;
            }
        }
        return vector<int> (powerful.begin(), powerful.end());
    }
};
```
