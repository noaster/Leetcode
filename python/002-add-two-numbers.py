"""
Problem : Add Two Numbers (https://leetcode.com/problems/add-two-numbers/description/)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """Solution Class"""

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(0)
        next_result = result
        while True:
            next_result.val, carry = Solution.add_nodes(l1, l2, carry)
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

            if l1 == None and l2 == None and carry == 0:
                break

            prev_result = next_result
            next_result = ListNode(0)
            prev_result.next = next_result

        return result
    @staticmethod
    def add_nodes(l1, l2, carry):
        sum_numbers = carry
        if l1 != None:
            sum_numbers += l1.val
        if l2 != None:
            sum_numbers += l2.val
        return [sum_numbers % 10, sum_numbers // 10]