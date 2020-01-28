---
category: Leetcode
---

https://leetcode.com/problems/largest-time-for-given-digits/

1. Problem Analysis
  - With given four digit make the latest time in 24 hr system.
  
2. Prerequisite
  - Maybe better with pre-defined array storing maximum available number
  - Need to store what digit is available?

3. N.B
  - Maximum possible digit is different by it's position.

4. Plan
  - ~count the digit~
  - ~from the left to right in time system, get the possible maximum digit~
  - make all possible combination and get max

5. Result
  - 4ms. 63.61%, 8.4MB 50%
  
  maybe possible without sort + next_permutation and it will possibly reduce time complexity.
  
```
class Solution {
private:
    bool check_valid_time(string time) {
        if( time[0] > '2' ){
            return false;
        } else if ( time[0] == '2' ) {
            if( time[1] > '3' ){
                return false;
            }
        }
        
        if( time[2] > '5' ){
            return false;
        }
        return true;
    }
    
    string get_max_time(string t1, string t2) {
        bool greater = true;
        for( int i = 0 ; i < 4; ++i ) {
            if( t1[i] < t2[i] ){
                greater = false;
                break;
            }
        }
        if( !greater )
            return t2;
        return t1;
    }
public:
    string largestTimeFromDigits(vector<int>& A) {
        string ret = "00:00";
        vector<int> time(4, 0);
        
        string tmp = "0000";
        for( int i = 0 ; i < 4; ++i ) {
            tmp[i] += A[i];
        }
        
        sort(tmp.begin(), tmp.end());
        string maxtime = "0000";
        bool notfound = true;
        do {
            if(check_valid_time(tmp)) {
                maxtime = get_max_time(maxtime, tmp);
                notfound = false;
            }
        }while( next_permutation(tmp.begin(), tmp.end()));
        
        if( notfound )
            return "";
        
        ret[0] = maxtime[0];
        ret[1] = maxtime[1];
        ret[3] = maxtime[2];
        ret[4] = maxtime[3];
        
        return ret;
    }
};
```
