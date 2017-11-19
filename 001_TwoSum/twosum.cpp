/*
Problem : Two Sum (https://leetcode.com/problems/two-sum/description/)
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