"""
Problem : Two Sum (https://leetcode.com/problems/two-sum/description/)
"""
class Solution(object):
    """Solution Class"""
    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for i, value in enumerate(nums):
            num = target - value
            if num in num_dict:
                return [num_dict[num], i]
            else:
                num_dict[value] = i

        return []
