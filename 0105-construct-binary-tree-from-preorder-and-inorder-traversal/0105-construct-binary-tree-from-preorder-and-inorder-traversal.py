# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildBTree(self, parent: TreeNode, preorder: List[int], inorder: List[int], preIdx: List[int], isLeft: bool) -> Optional[TreeNode]:
        if preIdx[0] >= len(preorder):
            return None
        if not preorder[preIdx[0]] in inorder:
            return None
        node = TreeNode(preorder[preIdx[0]])
        preIdx[0] += 1
        
        if parent != None and isLeft and parent.left == None:
            parent.left = node
            
        if parent != None and not isLeft and parent.right == None:
            parent.right = node
        
        idx = inorder.index(node.val)
        self.buildBTree(node, preorder, inorder[:idx], preIdx, True)
        self.buildBTree(node, preorder, inorder[idx + 1:], preIdx, False)
        return node
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = [0]
        root = self.buildBTree(None, preorder, inorder, preIdx, True)
        return root