class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for i in range(len(nums)):
            num = target - nums[i]
            if num in num_dict:
                return [num_dict[num], i]
            else:
                num_dict[nums[i]] = i

        return []
