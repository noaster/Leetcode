/*
Problem : Two Sum (https://leetcode.com/problems/two-sum/description/)
Find indices of the two numbers (input-0) that they add up to a target (input-1)

Example : 
  - Input-0 : [2, 7, 11, 15]
  - Input-1 : 9
  - Output : [1, 2]
*/
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> results;
        
        int vecSize = nums.size();
        for (int i = 0; i < vecSize; ++i)
        {
            for (int j = i + 1; j < vecSize; ++j)
            {
                if (nums[i] + nums[j] == target)
                {
                    results.push_back(i);
                    results.push_back(j);
                }
            }
        }

        return results;
    }
};
