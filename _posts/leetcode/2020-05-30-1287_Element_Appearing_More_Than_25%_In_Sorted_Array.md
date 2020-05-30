---
category: Leetcode
---

[element-appearing-more-than-25-in-sorted-array](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/)

1. Problem Analysis
  - Find one dominant (which appers more than 25%)
  
2. Prerequisite
  - array is sorted in ascending order
  - there is only one dominant value always

3. N.B
  - Binary search
  - Divide & conquer

4. Plan
  - Binary search problem
  - Check minimum or maximum value could be dominant
  - By dividing array half, check whether the mid value is dominant
  - Finding the number of occurrence uses binary search
  
5. Result
  - 20ms. 74.1%, 12.6MB 100% Cannot find anymore optimal solution.

```cpp
class Solution {
private:
    int binary_search(vector<int> &arr, int value, int lo, int hi) {
        int mid;
        while( hi > lo + 1 ) {
            mid = (lo + hi ) / 2;
            if( arr[mid] < value ) { 
                if( arr[mid + 1] == value )
                    return mid + 1;
                lo = mid;
            } else if( arr[mid] > value ) {
                if( arr[mid - 1] == value )
                    return mid;
                hi = mid;
            } else {
                if( arr[mid - 1] < value )
                    return mid;
                if( arr[mid + 1] > value )
                    return mid + 1 ;
                if( arr[lo] == value )
                    lo = mid;
                else if( arr[hi] == value)
                    hi = mid;
            }
        }
        return hi;
    }
    
    int count(vector<int> &arr, int index, int value, int lo, int hi) {
        int start = index;
        if( arr[lo] == value )
            start = lo;
        else
            start = binary_search(arr, value, lo, index);
        
        int end = index;
        if( arr[hi - 1] == value )
            end = hi;
        else {
            end = binary_search(arr, value, index, hi);
        }
        return end - start;
    };
    
    int search_dominant(vector<int> &arr, int lo, int hi, int standard) {
        if( hi <= standard + lo )
            return -1;
        
        int result = -1;
        int mid = (lo + hi) / 2;
        
        int c = count( arr, mid, arr[mid], lo, hi);
        if( c > standard )
            return mid;
        
        result = search_dominant(arr, lo, mid, standard);
        if( result > 0 )
            return result;
        
        return search_dominant(arr, mid, hi, standard);
    }
public:
    int findSpecialInteger(vector<int>& arr) {
        int len = arr.size();
        if( len < 4 ) 
            return arr[0];
        
        int standard = len >> 2;
        int value;
        if( arr[standard] == arr[0] )
            return arr[0];
        if( arr[len - 1] == arr[len - standard - 1 ])
                return arr[len -1];
        return arr[search_dominant(arr, 0, len, standard)];
    }
};
```
