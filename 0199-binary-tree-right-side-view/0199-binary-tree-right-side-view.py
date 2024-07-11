# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node: Optional[TreeNode], rightSizes: [int], level: int):
        if node == None:
            return
        rightLength = len(rightSizes)
        if rightLength == level:
            rightSizes.append(node.val)
        if node.right != None:
            self.traverse(node.right, rightSizes, level + 1)
        if node.left != None:
            self.traverse(node.left, rightSizes, level + 1)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSizes = []
        self.traverse(root, rightSizes, 0)
        return rightSizes