/*
Problem : https://leetcode.com/problems/median-of-two-sorted-arrays/description/
Find the median of the two sorted arrays.
(Time complexity : O(log(m+n)))

Input-0 : [1, 3]
Input-1 : [2]
Output : 2.0
*/

#include <vector>
using namespace std;
// time complexity of this solution is O(m+n)
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int num1Size = nums1.size();
        int num2Size = nums2.size();
        
        int medianIndex[2] = {0};
        medianIndex[0] = ((num1Size + num2Size) / 2) - !((num1Size + num2Size) % 2);
        medianIndex[1] = medianIndex[0] + !((num1Size + num2Size) % 2);

        double medianValue[2] = {0.0, 0.0};
        vector<int>::const_iterator it1 = nums1.begin(), it2 = nums2.begin();
        for (int i = 0; i <= medianIndex[1]; ++i)
        {
            int value = 0;
            if (it1 == nums1.end())
            {
                value = *it2++;
            }
            else if (it2 == nums2.end())
            {
                value = *it1++;
            }
            else if (*it1 < *it2)
            {
                value = *it1++;
            }
            else
            {
                value = *it2++;
            }

            if (i == medianIndex[0])
            {
                medianValue[0] = value;
            }
            if (i == medianIndex[1])
            {
                medianValue[1] = value;
            }
        }

        return (medianValue[0] + medianValue[1]) / 2;
    }
};
