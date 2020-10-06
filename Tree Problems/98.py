# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.result = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.result.append(root.val)
            inorder(root.right)
        #preform an inorder traversal and build a list called resuult
        #check if result is sorted
        #if so return True, else return false
        #solution can be optimized, don't need to store all of the tree values, only need the value just traversed during inorder traversal
        inorder(root)
        for i in range(1, len(self.result)):
            if self.result[i] <= self.result[i-1]:
                return False
        return True