---
category: Leetcode
---

[two-city-scheduling](https://leetcode.com/problems/two-city-scheduling/)

1. Problem Analysis
  - For 2N people devide them to two city to make total price minimum
  
2. Prerequisite
  - sort by diffrence of cost to cities for each person by descending order

3. N.B

4. Plan
  - sort by difference of cost by descending order
  - take at most N people for each city from the first
  - accumulate costs during taking people
  - O(nlogn) from sorting
  
5. Result
  - 4ms. 88%, 8.5MB 100%

```cpp
class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        sort(costs.begin(), costs.end(), [] (vector<int> &a, vector<int> &b) {
            return abs(a[1] - a[0]) < abs(b[1] - b[0]) ? false : true;
        });
        vector<int> count(2, 0);
        int len = costs.size();
        int total_cost = 0;
        int N = len / 2;
        int index;
        for( index = 0 ; index < len && count[0] < N && count[1] < N ; ++index ) {
            if( costs[index][0] < costs[index][1] ) {
                total_cost += costs[index][0];
                count[0]++;
            } else if( costs[index][1] < costs[index][0] ) {
                total_cost += costs[index][1];
                count[1]++;
            } else {
                total_cost += costs[index][0];
                count[0] > count[1] ? count[1]++ : count[0]++;
            }
        }
        
        for( int i = 0 ; i < 2; ++i ) {
            for( int j = count[i] ; j < N ; ++j ) {
                total_cost += costs[index++][i];
            }
        }
        
        return total_cost;
        
    }
};
```
