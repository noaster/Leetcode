class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size();
        if (size <= 0) {
          return 0;
        }
        int tmp;
        int endIndex = size - 1;
        for (int i = 0; i <= endIndex; ++i) {
            if (nums[i] == val) {
                while (endIndex > i && nums[endIndex] == val) {
                    endIndex--;
                }
                if (endIndex <= i) {
                    break;
                }
                tmp = nums[i];
                nums[i] = nums[endIndex];
                nums[endIndex] = tmp;
            }
        }
        if (nums[endIndex] != val) {
          endIndex++;
        }
        return endIndex;
    }
};